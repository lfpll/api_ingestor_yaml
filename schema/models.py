from typing import Dict, List, Optional

from pydantic import BaseModel


class Column(BaseModel):
    nullable: Optional[bool] = False
    type: str
    # Renamed from valid_types for consistency
    valid_types: Optional[List[str]] = []


class Schema(BaseModel):
    COLUMNS: Dict[str, Column]
