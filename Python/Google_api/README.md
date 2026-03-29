# Readme

## First time Here?

1. Set up the expected environment.
   1. Python3.14 (this can be easily done with Conda (anaconda) if you have it installed)
      1. if you don't have Python 3.14 installed, either install it or create a virtual env with it, using conda.
         1. `conda env create -f environment.yml`
   2. UV (for handling virtual environment)
      1. `uv venv .venv`
      2. `uv sync`

## How to RUN ?

0. `conda activate google_api_env` (only if your default python isn't 3.14)
1. `source .venv/bin/activate` # activate UV virtual env for installing dependencies
2. `python -m scripts.<\main or any of the other files such as google_sheets>`
3. For running pytest files (./tests/test\*.py)
   1. `uv run pytest`

## What to run ?

This "Example Project" is for learning and creating snippets for working with Google Cloud (GCP) API, which enables us to interact with e.g Google Sheets, Google Drive, Google XYZ. But in order to do so, one needs to have a GCP account, create a project, and enable the desired API. Also this example expects/requires that you create a service account, and downloads the service-account-credentials file.

When these pre-requisites are met, you can run the test/example code found in `./scripts/`.
E.g for creating a google api client that can interacte with the apis, I have created a separate file, `google_client` that the other examples use.

If you want to check out the `Google Sheets API` then the file ./scripts/google*sheets is the one you're looking for. So to recap,
in ./scripts directory. all files that interact with the google api, have a prefix `google*`and then the "api" they use. So for Sheets, the example is`./scripts/google_sheets.py`.

To run you'll need to add a `.env` file (see `.env.template`) and then have python3.14, uv virtual environment installed, activated and synced. Then you can run `uv run python -m scripts.<example_file_no_fileextention>` -> `uv run python -m scripts.google_sheets`
