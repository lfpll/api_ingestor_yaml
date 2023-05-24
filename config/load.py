import yaml
from pydantic import FilePath

from config.models import Auth, Config, Endpoint, GlobalSettings


def load_config(yaml_path: FilePath) -> Config:

    # Load the YAML configuration file
    with open(yaml_path) as file:
        raw_config = yaml.safe_load(file)

    # Parse it into the dataclasses
    auth = Auth(**raw_config['AUTH'])
    global_settings = GlobalSettings(**raw_config['GLOBAL_SETTINGS'])

    # get's the endpoints and their children
    endpoints = {name: Endpoint(**config)
                 for name, config in raw_config['ENDPOINTS'].items()}

    config = Config(AUTH=auth,
                    GLOBAL_SETTINGS=global_settings,
                    ENDPOINTS=endpoints)

    for endpoint in config.ENDPOINTS.values():
        endpoint.propagate_default_config_to_child()

    return config
