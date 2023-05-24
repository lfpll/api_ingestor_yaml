from schema.models import Schema
from typing import Dict, List
import os
import yaml
from pydantic import FilePath

# load and parse YAML schema
def list_schemas(schema_folder: FilePath) -> List[FilePath]:
    files = []
    for f in os.listdir(schema_folder):
        file_name = os.path.join(schema_folder, f)
        if os.path.isfile(file_name) and file_name.endswith('.yaml'):
            files.append(file_name)
    
    return files

def load_schemas(schemas_list: List[FilePath]) -> Dict[str, Dict[str, str]]:
    schemas = {}
    for file_path in list_schemas(schemas_list):
        with open(file_path, 'r') as file:
            name = file_path.split('/')[-1].split('.')[0]
            schema = yaml.safe_load(file)
            schemas[name] = Schema(**schema)
    
    return schemas

