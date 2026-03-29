# To see print statements during test runs, use:
# uv run pytest -s -- tests/test_gcp_sheet_read.py

import pytest
from unittest.mock import patch, MagicMock

from scripts.google_client import check_impoort_wrk


def test_abc():
    assert check_impoort_wrk() == 1


from scripts.google_client import build_google_service

from scripts.google_sheets import (
    _read_sheet,
    _get_sheet_tabs,
)


### ---------------------------------------------------------------------
### Fake Credentials to bypass Google auth internals
### ---------------------------------------------------------------------
class FakeCreds:
    universe_domain = "googleapis.com"

    def with_scopes(self, scopes):
        return self

    def create_scoped(self, scopes=None):
        return self

    def authorize(self, http=None):
        class Authorized:
            credentials = FakeCreds()

        return Authorized()


### ---------------------------------------------------------------------
### Test constants
### ---------------------------------------------------------------------
fake_service_account_json_str = """
{
  "type": "service_account",
  "project_id": "dummy-project",
  "private_key_id": "test-private-key-id",
  "private_key": "-----BEGIN PRIVATE KEY-----\\nFAKE_PRIVATE_KEY_DATA\\n-----END PRIVATE KEY-----\\n",
  "client_email": "fake-service-account@dummy-project.iam.gserviceaccount.com",
  "client_id": "123456789012345678901",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/fake-service-account%40dummy-project.iam.gserviceaccount.com"
}
"""

TAB_NAME = "My_Tab_Name"

mock_sheet_api_response = {
    "range": f"{TAB_NAME}!A1:BH3",
    "majorDimension": "ROWS",
    "values": [
        ["Header1", "Header2", "Header3"],
        ["row1col1", "", "row1col3"],
        ["row2col1", "row2col2", ""],
    ],
}


### ---------------------------------------------------------------------
### Pytest fixtures
### Pytest fixtures are functions that provide a defined, reliable, and consistent baseline (setup and teardown) context for tests
### ---------------------------------------------------------------------


@pytest.fixture
def mock_google_sheet_service():
    """
    Fixture that patches Google API build() + credentials
    and returns a ready-to-use MagicMock Sheets service.
    """
    with (
        patch(
            "scripts.google_client.Credentials.from_service_account_info",
            return_value=FakeCreds(),
        ) as _mock_creds,
        patch("scripts.google_client.build") as mock_build,
    ):
        mock_service = MagicMock()
        mock_build.return_value = mock_service

        yield mock_service  # value injected into tests


### ---------------------------------------------------------------------
### Tests
### ---------------------------------------------------------------------


def test_read_sheet(mock_google_sheet_service):
    # Set the fake Sheets API response
    mock_google_sheet_service.spreadsheets().values().get().execute.return_value = (
        mock_sheet_api_response
    )

    # Build the service using our mocked creds + build()
    service = build_google_service(fake_service_account_json_str)

    # Ensure build() returned our MagicMock service
    assert service is mock_google_sheet_service

    # Now call the read function
    rows = _read_sheet(service, "123", TAB_NAME)

    assert rows == [
        ["Header1", "Header2", "Header3"],
        ["row1col1", "", "row1col3"],
        ["row2col1", "row2col2", ""],
    ]

    print("\n_read_sheet returned rows:", rows)


def test_get_sheet_tabs(mock_google_sheet_service):
    # Mock Google Sheets "sheets metadata" response
    mock_google_sheet_service.spreadsheets().get().execute.return_value = {
        "sheets": [
            {"properties": {"title": TAB_NAME}},
            {"properties": {"title": "Sheet2"}},
            {"properties": {"title": "OtherTab"}},
        ]
    }

    service = build_google_service(fake_service_account_json_str)

    tabs = _get_sheet_tabs(service, "SPREADSHEET_ID_123")

    assert tabs == [TAB_NAME, "Sheet2", "OtherTab"]

    print("\n_get_sheet_tabs returned:", tabs)


def test_read_sheet_and_convert_to_dict_safe_ansible(
    mock_google_sheet_service, monkeypatch
):
    """
    Tests the full flow of read_sheet_and_convert_to_dict_safe:
    - Reads env var for creds
    - Builds service (mocked)
    - Gets sheet tabs (mocked)
    - Reads sheet values (mocked)
    - Converts values to dicts

    # Expected outcome
    Each row in Sheet, becomes a a dict in a list.
    Row dict keys = column headers., values = cell values.
    """

    # Import here so we can monkeypatch properly
    from scripts.google_sheets import read_sheet_and_convert_to_dict_safe

    # Set the environment variable required by the function
    monkeypatch.setenv(
        "GOOGLE_SHEETS_SERVICE_ACCOUNT_JSON", fake_service_account_json_str
    )
    monkeypatch.setenv("CI", "false")

    # --- Mock #1: _get_sheet_tabs ---
    # Pretend the spreadsheet has 3 tabs
    mock_google_sheet_service.spreadsheets().get().execute.return_value = {
        "sheets": [
            {"properties": {"title": TAB_NAME}},
            {"properties": {"title": "OtherTab"}},
        ]
    }

    # --- Mock #2: _read_sheet ---
    mock_google_sheet_service.spreadsheets().values().get().execute.return_value = {
        "values": [
            ["Header1", "Header2", "Header3"],
            ["row1col1", "", "row1col3"],
            ["row2col1", "row2col2", ""],
        ]
    }

    # Act
    content = read_sheet_and_convert_to_dict_safe(
        spreadsheet_id="SPREAD123",
        tab=TAB_NAME,  # explicit
        _range=None,
    )

    # Expected dict output after _convert_sheet_values_to_dict
    expected = [
        {"Header1": "row1col1", "Header2": "", "Header3": "row1col3"},
        {"Header1": "row2col1", "Header2": "row2col2", "Header3": ""},
    ]

    assert content == expected

    print("\nread_sheet_and_convert_to_dict_safe (ansible) returned:", content)


def test_read_sheet_and_convert_to_dict_safe_ci(mock_google_sheet_service, monkeypatch):
    """
    Tests the CI flow of read_sheet_and_convert_to_dict_safe:
    - Reads env var for CI
    - Does not builds service (mocked)
    - returns empty list in CI

    # Expected outcome
    Each row in Sheet, becomes a a dict in a list.
    Row dict keys = column headers., values = cell values.
    """

    # Import here so we can monkeypatch properly
    from scripts.google_sheets import read_sheet_and_convert_to_dict_safe

    # Set the environment variable required by the function, to overwrite in CI
    # ENV VAR set by default by Github Actions
    monkeypatch.setenv("CI", "true")

    content = read_sheet_and_convert_to_dict_safe(
        spreadsheet_id="SPREAD123",
        tab=TAB_NAME,  # explicit
        _range=None,
    )

    assert content == []
    print("\nread_sheet_and_convert_to_dict_safe (ci) returned:", content)
