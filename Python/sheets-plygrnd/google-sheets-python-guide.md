
# 📘 Minimal & Secure Guide: Reading a Google Sheet in Python

## 🛠️ 1. Install required packages

```bash
pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

---

## 🔐 2. Authentication Method (Recommended)

### ✅ Use a Service Account  
Best for scripts, servers, cron jobs, CI/CD, or backend apps.

#### Steps:
1. Create a **Service Account** in Google Cloud Console.  
2. Download the **JSON key file** (keep it secret — do NOT commit it).  
3. Share the Google Sheet with the service account email:  
   ```
   your-service-account@PROJECT-ID.iam.gserviceaccount.com
   ```
   Give it **Viewer** permission.

---

## 📄 3. Minimal & Secure Python Script

```python
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

# ---- CONFIG ----
SERVICE_ACCOUNT_FILE = "service-account.json"  # Do NOT commit this file
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

SPREADSHEET_ID = "YOUR_SHEET_ID"
RANGE_NAME = "Sheet1!A1:C10"

# ---- AUTH ----
credentials = Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES,
)

# ---- API CLIENT ----
service = build("sheets", "v4", credentials=credentials)

# ---- READ SHEET ----
sheet = service.spreadsheets()
result = sheet.values().get(
    spreadsheetId=SPREADSHEET_ID,
    range=RANGE_NAME
).execute()

values = result.get("values", [])

print(values)
```

---

## 🔐 4. Security Best Practices

### ❌ Never commit service-account.json  
Add to `.gitignore`:

```
service-account.json
*.pem
*.p12
```

---

### 🔒 Avoid storing secrets on disk (use env variables)

**Shell:**

```bash
export GOOGLE_APPLICATION_CREDENTIALS_JSON="$(cat service-account.json)"
```

**Python:**

```python
import json
import os
from google.oauth2.service_account import Credentials

creds_dict = json.loads(os.environ["GOOGLE_APPLICATION_CREDENTIALS_JSON"])
credentials = Credentials.from_service_account_info(creds_dict)
```

This prevents the key file from existing on disk in production.

---

## 📦 5. Optional: Simple Helper Function

```python
def read_sheet(sheet_id: str, range_: str):
    creds = Credentials.from_service_account_file(
        "service-account.json",
        scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"]
    )
    service = build("sheets", "v4", credentials=creds)
    return (
        service.spreadsheets()
        .values()
        .get(spreadsheetId=sheet_id, range=range_)
        .execute()
        .get("values", [])
    )

rows = read_sheet("YOUR_SHEET_ID", "Sheet1!A1:C10")
print(rows)
```

---

## 🛡️ 6. Summary

| Need | Solution |
|------|----------|
| Secure access | Service Account w/ read-only scope |
| Minimal code | ~20 lines |
| Production compatible | Yes |
| Official Google libs | Yes |

---

If you want, I can include extra sections such as:  
📌 Restricting service accounts to only one Sheet  
📌 Using Docker securely  
📌 Async version using aiohttp or aiogoogle  
📌 A template project folder structure  
