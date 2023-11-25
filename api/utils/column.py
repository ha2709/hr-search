import os
import json

# Get the directory path of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(current_dir, "..", "company_config.json")


def get_company_display_columns(company_name: str):
    # Load the configuration from the JSON file
    with open(json_file_path, "r") as file:
        config_data = json.load(file)

    return config_data.get(company_name, [])
