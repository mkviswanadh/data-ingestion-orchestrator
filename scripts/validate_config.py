import os
import yaml
import json
import sys
from jsonschema import validate, ValidationError

def main():
    schema_path = os.path.join(os.path.dirname(__file__), '..', 'config-schema', 'ingestion_schema.json')
    with open(schema_path) as f:
        schema = json.load(f)

    # validate all configs in configs folder
    config_dir = os.path.join(os.getcwd(), 'configs')
    if not os.path.exists(config_dir):
        print("No configs directory found.", file=sys.stderr)
        sys.exit(1)

    errors = False
    for fname in os.listdir(config_dir):
        if fname.endswith('.yaml') or fname.endswith('.yml'):
            path = os.path.join(config_dir, fname)
            with open(path) as cf:
                data = yaml.safe_load(cf)
            try:
                validate(instance=data, schema=schema)
                print(f"{fname} OK")
            except ValidationError as e:
                print(f"{fname} FAILED: {e}", file=sys.stderr)
                errors = True
    if errors:
        sys.exit(1)

if __name__ == "__main__":
    main()

