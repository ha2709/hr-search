 
import os
from fastapi import APIRouter, Depends, HTTPException
import json
from typing import List


company_router = APIRouter()
# Get the directory path of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(current_dir, '..', 'company_config.json')


def get_company_display_columns(company_name: str):
    # Load the configuration from the JSON file
    with open(json_file_path, 'r') as file:
        config_data = json.load(file)

    # Get the display columns for the specified company
   
    return config_data.get(company_name, [])


@company_router.get("/companies")
async def get_company_list():
    # Load the configuration from the JSON file
    with open(json_file_path, 'r') as file:
        config_data = json.load(file)

    # Return the list of company name
    return list(config_data.keys())

@company_router.get("/companies/{company_name}", response_model=List[str])
async def get_company_info(display_columns: List = Depends(get_company_display_columns, use_cache=True)):
 
    return display_columns
