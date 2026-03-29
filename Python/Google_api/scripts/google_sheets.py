#!/usr/bin/env python3
import os
import sys
from typing import Any, TypedDict
import yaml

from .google_client import build_google_service

# --- vvv Google Sheets API imports ---
from googleapiclient.discovery import Resource
from googleapiclient.errors import HttpError
# --- ^^^ Google Sheets API imports ---


class GoogleSheetConfig(TypedDict):
    spreadsheet_id: str
    tab: str


GOOGLE_SHEETS_SERVICE_ACCOUNT_JSON = "GOOGLE_SHEETS_SERVICE_ACCOUNT_JSON"
# GOOGLE_SHEETS_SERVICE_ACCOUNT_JSON = "GOOGLE_SHEETS_SERVICE_ACCOUNT_JSON_FAKE"

DEFAULT_TAB_NAME_NORWEGIAN = "Ark 1"


def _debug_print(message: str):
    """
    Printing to stdout would interfere with Ansible module output,
    and break Ansible/Module communication. Hence, we print to stderr.
    """
    print(f"[Package_Inventory.py]: {message}", file=sys.stderr)


def _get_sheet_tabs(service: Resource, SPREADSHEET_ID: str):
    sheet_metadata = service.spreadsheets().get(spreadsheetId=SPREADSHEET_ID).execute()
    tabs = []
    for tab in sheet_metadata["sheets"]:
        tab_name = tab["properties"]["title"]
        tabs.append(tab_name)
    return tabs


def _read_sheet(
    service: Resource,
    spreadsheet_id: str,
    tab: str | None = None,
    _range: str | None = None,
) -> list[any]:
    """
    Docs: https://developers.google.com/workspace/sheets/api/reference/rest
    """
    # specify the tab and optional range to read
    tab_range = f"{tab}!{_range}" if _range else f"{tab}"
    result = {}
    try:
        # sheet = service.spreadsheets()
        # values = sheet.values() # returns ValueRange resource # # https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets.values#resource:-valuerange
        # request = values.get(spreadsheetId=spreadsheet_id, range=tab_range)  # returns Range of values, and only get non-empty cells, params: https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets.values/get#query-parameters
        # result = request.execute() # actually execute the request, and get the response
        result = (
            service.spreadsheets()
            .values()
            .get(
                spreadsheetId=spreadsheet_id,
                range=tab_range,
            )
            .execute()  # response is a Python object built from the JSON response sent by the API server.
        )
    except HttpError as e:
        print(
            "Error response status code : {0}, reason : {1}".format(
                e.status_code, e.error_details
            )
        )

    return result.get("values", [])


def _convert_sheet_values_to_dict(values: list[list[Any]]) -> list[dict[str, Any]]:
    """
    Convert Google Sheets API tab `values` (as returned by `_read_sheet`);
    - First row is treated as headers
    - Subsequent rows are zipped with headers to produce dicts
    - Missing trailing cells are treated as empty strings
    - Extra cells beyond headers are ignored

    Args:
        values: A list of rows, where each row is a list of cell values.

    Returns:
        A list of dictionaries mapping header -> cell value.
        Where each list element/dictionary is a row in the sheet, represented as a dict.
    """
    if not values:
        return []

    headers = [str(h) if h is not None else "" for h in values[0]]
    data_rows = values[1:]

    result: list[dict[str, Any]] = []
    for row in data_rows:
        # Normalize row length to headers length
        if len(row) < len(headers):
            row = row + [""] * (len(headers) - len(row))
        elif len(row) > len(headers):
            row = row[: len(headers)]

        # Cast all values to strings for parity with CSV reader behavior
        normalized = [str(v) if v is not None else "" for v in row]
        result.append(dict(zip(headers, normalized)))

    return result


def read_sheet_and_convert_to_dict(
    spreadsheet_id: str, tab: str, _range: str | None = None
) -> list[dict[str, Any]]:
    # GOOGLE_SHEETS_SERVICE_ACCOUNT_JSON is expected to be set in the environment by Vault & `.envrc`
    service_account_credentials_file_as_json_str = os.environ.get(
        GOOGLE_SHEETS_SERVICE_ACCOUNT_JSON
    )

    ### Set defaults
    spreadsheet_id = spreadsheet_id or None
    tab = tab or DEFAULT_TAB_NAME_NORWEGIAN
    _range = _range or None  # "A1:C10"

    # Build the Sheets API service
    service = build_google_service(service_account_credentials_file_as_json_str)
    _tabs = _get_sheet_tabs(service, spreadsheet_id)

    # _debug_print(f"Tabs in spreadsheet: {_tabs}")
    # _debug_print(f"Reading tab: {tab}, range: {_range or 'entire tab'}")

    values = _read_sheet(service, spreadsheet_id, tab, _range)
    # _debug_print(json.dumps({"values": values}, indent=2))
    content = _convert_sheet_values_to_dict(values)
    # _debug_print(content)

    return content


def read_sheet_and_convert_to_dict_safe(*args, **kwargs):
    """
    returns a 1d list of dicts.
    Each list element is a row in the sheet, represented as a dict.
    The row-dict maps column header to cell value.
    """
    IS_CI = os.getenv("CI") == "true"
    HAS_CREDENTIALS = os.getenv(GOOGLE_SHEETS_SERVICE_ACCOUNT_JSON) is not None

    if IS_CI:
        return []
    elif not HAS_CREDENTIALS:
        _debug_print(
            f"Warning: Environment variable '{GOOGLE_SHEETS_SERVICE_ACCOUNT_JSON}' not set, skipping Google Sheets read.",
        )
        return []
    return read_sheet_and_convert_to_dict(*args, **kwargs)


def read_google_spreadsheet_config(path: str) -> list[GoogleSheetConfig] | None:
    try:
        with open(path, "r") as f:
            return yaml.safe_load(f) or []
    except FileNotFoundError:
        raise RuntimeError(f"YAML file not found: {path}")
    except yaml.YAMLError as e:
        raise RuntimeError(f"Invalid YAML in {path}: {e}")


if __name__ == "__main__":
    from pathlib import Path
    from dotenv import load_dotenv

    load_dotenv()  # Load environment variables from .env file

    inventory_dir = Path(__file__).parent
    print(f"Inventory directory: {inventory_dir}")
    gcp_sheet_config_path = inventory_dir / "_package_inventory_config.yml"
    print(
        f"GCP sheet config path: {gcp_sheet_config_path}",
        f"Exists: {gcp_sheet_config_path.exists()}",
    )
    gcp_sheets_config: list[GoogleSheetConfig] = read_google_spreadsheet_config(
        gcp_sheet_config_path
    )
    print(f"Config: {gcp_sheets_config}")

    spreadsheets = {}
    for gcp_sheet_config in gcp_sheets_config:
        sheet_id, tab = gcp_sheet_config["spreadsheet_id"], gcp_sheet_config["tab"]
        sheet_content = read_sheet_and_convert_to_dict_safe(sheet_id, tab)
        spreadsheets[f"{sheet_id}:{tab}"] = sheet_content
    print(f"Spreadsheets content: {spreadsheets}")
