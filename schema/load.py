import os
from typing import Dict, List

import yaml
from pydantic import FilePath

from schema.models import Schema


# load and parse YAML schema
def list_schemas(schema_folder: FilePath) -> List[FilePath]:
    files = []
    for f in os.listdir(schema_folder):
        file_name = os.path.join(schema_folder, f)
        if os.path.isfile(file_name) and file_name.endswith('.yaml'):
            files.append(file_name)

    return files


def load_schemas(schema_folder: List[FilePath]) -> Dict[str, Schema]:
    schemas = {}
    for file_path in list_schemas(schema_folder):
        with open(file_path) as file:
            name = file_path.split('/')[-1].split('.')[0]
            try:
                schema = yaml.safe_load(file)
                schemas[name] = Schema(COLUMNS=schema)
            except Exception as e:
                raise Exception(f"Error loading schema {file_path}: {e}")

    return schemas
