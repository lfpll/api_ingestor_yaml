from typing import Dict, List, Optional
from pydantic import BaseModel

class Column(BaseModel):
    null: bool
    type: str
    valid_values: Optional[List[str]]  # Renamed from valid_types for consistency

class Schema(BaseModel):
    COLUMNS: Dict[str, Column]

