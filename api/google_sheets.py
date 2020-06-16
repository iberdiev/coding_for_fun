# 1080335874057-0drqvm94a6pkligteke1edpnmqm2h83g.apps.googleusercontent.com
# zuAmbsgioBHSx71PGOlweKf-

# Step 1: Turn on the Google Sheets API + get cliendID + clientKey
# Step 2: Install the Google Client Library
#   pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

# from __future__ import print_function
# import pickle
# import os.path
# from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request

# # If modifying these scopes, delete the file token.pickle.
# SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# # The ID and range of a sample spreadsheet.
# SAMPLE_SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
# SAMPLE_RANGE_NAME = 'Class Data!A2:E'

# def main():
#     """Shows basic usage of the Sheets API.
#     Prints values from a sample spreadsheet.
#     """
#     creds = None
#     # The file token.pickle stores the user's access and refresh tokens, and is
#     # created automatically when the authorization flow completes for the first
#     # time.
#     if os.path.exists('token.pickle'):
#         with open('token.pickle', 'rb') as token:
#             creds = pickle.load(token)
#     # If there are no (valid) credentials available, let the user log in.
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 'credentials.json', SCOPES)
#             creds = flow.run_local_server(port=0)
#         # Save the credentials for the next run
#         with open('token.pickle', 'wb') as token:
#             pickle.dump(creds, token)

#     service = build('sheets', 'v4', credentials=creds)

#     # Call the Sheets API
#     sheet = service.spreadsheets()
#     result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#                                 range=SAMPLE_RANGE_NAME).execute()
#     values = result.get('values', [])

#     if not values:
#         print('No data found.')
#     else:
#         print('Name, Major:')
#         for row in values:
#             # Print columns A and E, which correspond to indices 0 and 4.
#             print('%s, %s' % (row[0], row[4]))

# if __name__ == '__main__':
#     main()
# pip install gspread oauth2client
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials

# # use creds to create a client to interact with the Google Drive API
# scope = ['https://spreadsheets.google.com/feeds']

# creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
# client = gspread.authorize(creds)

# # sheet = client.open("UCA_Transcripts").sheet1
# # print(help(client))
# print(client.list_spreadsheet_files())
# Extract and print all of the values
# list_of_hashes = sheet.get_all_records()
# print(list_of_hashes)

# import requests
# sheet_ID = '1i2-j3S8uqqOAmkDSGuSW41PaCWrFeqMnxTtnKg48rP0'
# URL = f'https://sheets.googleapis.com/v4/spreadsheets/{sheet_ID}'
# api_key = 'AIzaSyBp3dKJvSu9mgwY0H_KLNyI5OZXNEqqt1U'
# r = requests.get(URL, params={'key': api_key, 'ranges': "'Лист1'!A1:C10"})    
# print(r.text)

