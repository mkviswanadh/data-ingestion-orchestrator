#!/usr/bin/env python3

import os
import argparse
from llm_parser import parse_prompt
from config_writer import write_config
import requests

def main():
    parser = argparse.ArgumentParser(description="Onboard a new ingestion pipeline via LLM")
    parser.add_argument('--prompt', type=str, required=True, help='Prompt describing ingestion pipeline')
    parser.add_argument('--webhook-url', type=str, required=True, help='Webhook URL to send config for PR')
    args = parser.parse_args()

    metadata = parse_prompt(args.prompt)
    # metadata is dict, e.g. keys: pipeline_name, source, target, load_type

    config_filename = f"configs/{metadata['pipeline_name']}.yaml"
    write_config(metadata, config_filename)

    with open(config_filename, 'r') as f:
        content = f.read()

    payload = {
        "pipeline_name": metadata['pipeline_name'],
        "config_path": config_filename,
        "config_content": content
    }

    resp = requests.post(args.webhook_url, json=payload)
    print(f"Webhook response status: {resp.status_code}, body: {resp.text}")

if __name__ == "__main__":
    main()

