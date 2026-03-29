"""
This script is for testing the parsing of service account credentials from a JSON file into a JSON string, and then into a Python dictionary. It is useful for verifying that the credentials can be correctly read and parsed before using them in the Google Sheets API client.
usage: `python -m lib.parse_service_account_creds_to_json_str`
.
├── environment.yml
├── lib
│   └── parse_service_account_creds_to_json_str.py
├── main.py
├── scripts
├── service-account-creds.json
└── uv.lock
"""

from pathlib import Path
import json


def main(verbose: bool = False):
    project_root = Path(__file__).parent.parent
    credentials_file_path = project_root / "service-account-creds.json"
    found_file = credentials_file_path.exists()
    if verbose:
        print("Project root: ", project_root)
        print(
            f"Looking for service account credentials file at: {credentials_file_path}"
        )
        print(f"Found file {credentials_file_path}: {found_file}")
    if found_file:
        creds_json_str = credentials_file_path.read_text()
        creds = json.loads(creds_json_str)
        if verbose:
            print("Parsed credentials JSON:")
            print("----")
        print(json.dumps(creds))


if __name__ == "__main__":
    main()
