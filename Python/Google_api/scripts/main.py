from pathlib import Path

from google_sheets import (
    read_sheet_and_convert_to_dict_safe,
    read_google_spreadsheet_config,
)


def parse_from_google_sheets():
    content: list[dict[str, str]] = []
    inventory_dir = Path(
        __file__
    ).parent  # use __file__ to get symlink-inventory path, e.g iventory/lab_onboarding
    gcp_sheet_config_path = inventory_dir / "_package_inventory_config.yml"
    gcp_sheets_config = read_google_spreadsheet_config(gcp_sheet_config_path)

    for gcp_sheet_config in gcp_sheets_config:
        sheet_content = read_sheet_and_convert_to_dict_safe(
            gcp_sheet_config["spreadsheet_id"], gcp_sheet_config["tab"]
        )
        content.extend(sheet_content)


def main(): ...


if __name__ == "__main__":
    main()
