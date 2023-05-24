from typing import Dict, List, Optional

from pydantic import BaseModel, Field


class Auth(BaseModel):
    type: str = Field(...)
    token_name: str = Field(...)


class GlobalSettings(BaseModel):
    rate_limit: int = Field(...)
    retry_attempts: int = Field(...)
    timeout_seconds: int = Field(...)


class Mode(BaseModel):
    type: str = Field(...)
    incremental_column: str = Field(...)
    methodology: str = Field(...)
    pagination: Optional[Dict[str, str]]


class ErrorHandle(BaseModel):
    ignore: List[int] = Field(...)
    warning:  List[int] = Field(...)


class BaseEndpoint(BaseModel):
    HEADERS: Optional[Dict[str, str]] = None
    URL: Optional[str] = None
    HTTP_METHOD: Optional[str] = None
    MODE: Optional[Mode] = None
    CHILDREN_ARGUMENTS: Optional[Dict[str, str]] = None
    INSERT_CHILDREN: Optional[Dict[str, str]] = None
    CHILDREN: Optional[Dict[str, 'BaseEndpoint']] = None
    KEY_PROPERTIES: Optional[List[str]] = None
    ERROR_HANDLE: ErrorHandle


class Endpoint(BaseEndpoint):
    INITIAL_ARGUMENTS: Optional[Dict[str, List[str]]] = None

    def propagate_default_config_to_child(self,
                                          endpoint: Optional[BaseEndpoint]
                                          = None) -> None:
        propagate = ['HEADERS', 'HTTP_METHOD', 'MODE', 'INSERT_CHILDREN']
        # Propagates default parent endpoint configs
        if endpoint is None:
            endpoint = self
        if endpoint.CHILDREN is not None:
            for _, child in endpoint.CHILDREN.items():
                for key in propagate:
                    if getattr(child, key) is None:
                        father_val = getattr(endpoint, key)
                        setattr(child, key, father_val)
                self.propagate_default_config_to_child(child)
        return


class Config(BaseModel):
    AUTH: Auth
    GLOBAL_SETTINGS: GlobalSettings
    ENDPOINTS: Dict[str, Endpoint]

    def get_all_endpoint_names(self,
                               endpoints:
                               Optional[Dict[str, BaseEndpoint]]
                               = None,
                               names: List[str] = []) -> List[str]:
        # Get all the endpoint names
        if endpoints is None:
            endpoints = self.ENDPOINTS

        for name, endpoint in endpoints.items():
            if endpoint.CHILDREN is not None:
                names = self.get_all_endpoint_names(
                    endpoints=endpoint.CHILDREN,
                    names=names)
            names = [name] + names

        return names


BaseEndpoint.update_forward_refs()
