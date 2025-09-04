def write_sample_data(sheet):
    worksheet = sheet.sheet1
    worksheet.clear()
    worksheet.append_row(["Company Name", "Contact Person", "Website", "Industry", "Email Sent?"])

    sample_data = [
        ["Acme EdTech", "John Doe", "https://acme-edtech.com", "EdTech", "Not Sent"],
        ["LearnPro", "Jane Smith", "https://learnpro.io", "EdTech", "Not Sent"]
    ]

    for row in sample_data:
        worksheet.append_row(row)

# Run it
sheet = get_google_sheet()
write_sample_data(sheet)
print(f"Sheet URL: {sheet.url}")
