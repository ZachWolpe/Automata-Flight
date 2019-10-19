import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
# from test_import import main
import mission_control


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("Automata").sheet1


# Check for Emergency 
while True:
    list_of_hashes = sheet.get_all_records()
    status = list_of_hashes[-1]['Emergency Call']
    print(status)
    if (status == 'TRUE'):
        print(True)
        mission_control.main()
        break
    