import yaml
import os

def write_config(metadata: dict, filename: str):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as f:
        yaml.dump(metadata, f, sort_keys=False)

