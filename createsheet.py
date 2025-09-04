import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_google_sheet(sheet_name="Business Leads"):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)

    try:
        sheet = client.open(sheet_name)
    except gspread.SpreadsheetNotFound:
        # Create a new one if not found
        sheet = client.create(sheet_name)

    worksheet = sheet.sheet1

    # Optional: Share it with your Google account to view it in browser
    sheet.share('your-email@gmail.com', perm_type='user', role='writer')

    return sheet
create
