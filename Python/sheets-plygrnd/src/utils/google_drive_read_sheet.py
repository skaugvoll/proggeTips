#!/usr/bin/env python3
import json
import sys
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build, Resource
from googleapiclient.errors import HttpError


def test_import():
    print("Hello from google_drive_read_sheet.py! This is a test import function.")


def build_sheet_service(
    credentials_file: str,
) -> Resource | None:
    """
    Docs: https://developers.google.com/workspace/sheets/api/reference/rest
    """
    try:
        creds = Credentials.from_service_account_file(
            credentials_file,
            scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"],
        )
        service = build("sheets", "v4", credentials=creds)  # returns Resource object
        return service
    except Exception as e:
        print("Error creating Sheets service: ", e)
        return None


def get_sheet_tabs(service: Resource, SPREADSHEET_ID: str):
    sheet_metadata = service.spreadsheets().get(spreadsheetId=SPREADSHEET_ID).execute()
    tabs = []
    for tab in sheet_metadata["sheets"]:
        tab_name = tab["properties"]["title"]
        tabs.append(tab_name)
        print(tab_name)
    return tabs


def read_sheet(
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


if __name__ == "__main__":
    credentials_file = sys.argv[1]  # "/path/to/service-account.json"
    spreadsheet_id = sys.argv[2]  # "YOUR_SHEET_ID"
    tab = sys.argv[3] or "Sheet1"  # "Sheet1"
    _range = None  # "A1:C10"

    service = build_sheet_service(credentials_file)
    tabs = get_sheet_tabs(service, spreadsheet_id)

    print(f"Tabs in spreadsheet: {tabs}")
    print(f"Reading tab: {tab}, range: {_range or 'entire tab'}")

    values = read_sheet(service, spreadsheet_id, tab, _range)

    print(json.dumps({"values": values}, indent=2))
