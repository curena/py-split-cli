import json

from cli_app.common import constants
from splitapiclient.main import get_client
import logging
from requests import get, patch, post, put

defaultClient = get_client(constants.API_KEY)
logging.basicConfig(level=logging.DEBUG)

def get_client(api_key: str):
    foo: dict = {"apikey": api_key}
    logging.log(foo)
    return get_client(foo)

def list_all_splits(environments: dict):
    result = {}
    for environment in environments:
        result[environment] = get(
            f"{constants.SPLIT_BASE_URI}/splits/ws/{constants.WORKSPACE}/environments/{environment}",
            headers=constants.BASE_HEADERS,
        )
    return jsonify(result)


def get_split(split_name: str):
    return get(
        f"{constants.SPLIT_BASE_URI}/splits/ws/{constants.WORKSPACE}/{split_name}",
        headers=constants.BASE_HEADERS,
    ).json


def create_split(split_name: str, description: str):
    split_config = {
        "name": split_name,
        "description": description,
    }
    post(
        f"{constants.SPLIT_BASE_URI}/splits/ws/{constants.WORKSPACE}/trafficTypes/organization",
        headers=constants.BASE_HEADERS,
        data=split_config,
    )


def create_split_definition(split_name: str, environments: dict, definition: dict):

    # Assume received definition is valid for now
    if definition is None or len(definition) < 1:
        definition = default_treatment_definition()

    for environment in environments:
        post(
            f"{constants.SPLIT_BASE_URI}/splits/ws/{constants.WORKSPACE}/{split_name}/environments/{environment}",
            headers=constants.BASE_HEADERS,
            data=definition,
        )


def get_split_definition(split_name: str, environments: dict):
    result = {}
    for environment in environments:
        result[environment] = get(
            f"{constants.SPLIT_BASE_URI}/splits/ws/{constants.WORKSPACE}/{split_name}/environments/{environment}",
            headers=constants.BASE_HEADERS,
        )
    return jsonify(result)


def default_treatment_definition():
    return {
        "treatments": [default_on_treatment(), default_off_treatment()],
        "defaultTreatment": "off",
        "defaultRule": [{"treatment": "off", "size": 100}],
    }


def default_on_treatment():
    return {
        "name": "on",
        "configurations": "",  # Contingent on support for dynamic configs
        "description": "ENABLED status",
        "keys": [],
        "segments": [],
    }


def default_off_treatment():
    return {
        "name": "off",
        "configurations": "",  # Contingent on support for dynamic configs
        "description": "DISABLED status",
        "keys": [],
        "segments": [],
    }


def jsonify(result):
    json.dumps(result, sort_keys=True, indent=4)