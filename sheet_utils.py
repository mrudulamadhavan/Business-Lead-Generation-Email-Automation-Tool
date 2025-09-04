import gspread
from oauth2client.service_account import ServiceAccountCredentials

def write_to_google_sheet(data, sheet_name='Business Leads'):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    
    sheet = client.create(sheet_name)
    worksheet = sheet.sheet1
    worksheet.append_row(["Company Name", "Contact Person", "Website", "Industry", "Email Sent?"])

    for company in data:
        worksheet.append_row([
            company["Company Name"],
            company["Contact Person"],
            company["Website"],
            company["Industry"],
            "Not Sent"
        ])

    return sheet.url
