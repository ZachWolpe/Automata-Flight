import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
#import test_import
import mission_control


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("Automata").sheet1


# while True:
#     # Extract and print all of the values
#     list_of_hashes = sheet.get_all_records()
#     status = list_of_hashes[-1]['Emergency Call']
#     print(status)
#     if (status == 'TRUE'):
#         test_import.main()


# Check for Emergency 
list_of_hashes = sheet.get_all_records()
status = list_of_hashes[-1]['Emergency Call']
if (status == 'TRUE'):
    print(True)
    #test_import()
  #  mission_control()