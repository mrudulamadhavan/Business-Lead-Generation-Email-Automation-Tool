from scraper import scrape_startupwala
from sheet_utils import write_to_google_sheet
from email_sender import send_email
import gspread

# Step 1: Scrape
data = scrape_startupwala(industry="EdTech", city="Bangalore", num_pages=2)

# Step 2: Write to Google Sheets
sheet_url = write_to_google_sheet(data)
print(f"Data written to: {sheet_url}")

# Step 3: Send emails
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Business Leads").sheet1

rows = sheet.get_all_records()

for idx, row in enumerate(rows, start=2):  # Start from row 2 (row 1 is headers)
    website = row["Website"]
    if row["Email Sent?"] == "Not Sent":
        # Extract email if possible from website using an email-finding API, or skip
        sample_email = "bd@company.com"  # Placeholder

        success = send_email(
            to=sample_email,
            subject="Collaboration Opportunity",
            message_text=f"Hi, I'm reaching out to explore synergies with {row['Company Name']}."
        )
        sheet.update_cell(idx, 5, "Sent" if success else "Failed")
