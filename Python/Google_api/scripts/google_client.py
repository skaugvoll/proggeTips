#!/usr/bin/env python3
import json

# --- vvv Google Sheets API imports ---
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build, Resource
# --- ^^^ Google Sheets API imports ---


def check_impoort_wrk():
    return 1


def build_google_service(
    service_account_credentials_file_as_json_str: str, service_type: str = "sheets"
) -> Resource | None:
    """
    @param service_account_credentials_file_as_json_str: Service account credentials JSON as string
    @return: Google Sheets API service object

    Docs: https://developers.google.com/workspace/sheets/api/reference/rest
    """
    try:
        parsed_creds = json.loads(service_account_credentials_file_as_json_str)
        creds = Credentials.from_service_account_info(
            parsed_creds,
            scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"],
        )

        service = build(
            service_type, "v4", credentials=creds
        )  # returns Resource object
        return service
    except Exception as e:
        print("Error creating Sheets service: ", e)
        return None
