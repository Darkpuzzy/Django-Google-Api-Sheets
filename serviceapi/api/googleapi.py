from __future__ import print_function

from __future__ import print_function

import google.auth
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import pickle


class GoogleApi:
    SPREADSHEET_ID = '1M-qhu19fs8fUE8KjKTiGFxae4Ws69MgP9bsYyUHjxz4'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    service = None

    def __init__(self): # Init auth token.
        creds = None
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', self.SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials1.json', self.SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        # TODO ALTERNATIVE METHOD TAKE CREDS
        # creds = None
        # if os.path.exists('token.pickle'):
        #     with open('token.pickle', 'rb') as token:
        #         creds = pickle.load(token)
        #
        # if not creds or not creds.valid:
        #     if creds and creds.expired and creds.refresh_token:
        #         print('Hack')
        #         creds.refresh(Request())
        #     else:
        #         print('Flow')
        #         flow = InstalledAppFlow.from_client_secrets_file(
        #             'credentials1.json', self.SCOPES)
        #         creds = flow.run_local_server(port=0)
        #     with open('token.pickle', 'wb') as token:
        #         pickle.dump(creds, token)

        # Init service
        self.service = build('sheets', 'v4', credentials=creds)

    def updated_rows(self, rows, values):
        data = {
            'range': rows,
            'values': values
        }
        body = {
            'valueInputOption': "USER_ENTERED",
            'data': data
        }
        print('Hex')
        sheet = self.service.spreadsheets()
        result = sheet.values().batchUpdate(spreadsheetId=self.SPREADSHEET_ID, body=body).execute()
        print(f"{result} cells update.")

    def get_rows(self, range):
        try:
            sheet = self.service.spreadsheets()
            result = sheet.values().get(spreadsheetId=self.SPREADSHEET_ID,
                                        range=range).execute()
            values = result.get('values', [])

            if not values:
                print('No data found.')
                return

            print('Name, Major:')
            for row in values:
                # Print columns A and E, which correspond to indices 0 and 4.
                print('%s, %s, %s' % (row[0], row[1], row[2]))
        except HttpError as err:
            print(err)

    def update_title(self, title):
        try:
            requests = []
            # Change the spreadsheet's title.
            requests.append({
                'updateSpreadsheetProperties': {
                    'properties': {
                        'title': title
                    },
                    'fields': 'title'
                }
            })
            body = {
                'requests': requests
            }

            response = self.service.spreadsheets().batchUpdate(
                spreadsheetId=self.SPREADSHEET_ID,
                body=body).execute()
            return response
        except HttpError as error:
            print(f"An error occurred: {error}")
            return error

    def update_values(self, range_name, value_input_option, _values):
        try:
            values = [
                [
                    # Cell values ...
                ],
                # Additional rows ...
            ]
            body = {
                'values': values,
                "majorDimension": "ROWS"
            }
            result = self.service.spreadsheets().values().update(
                spreadsheetId=self.SPREADSHEET_ID, range=range_name,
                valueInputOption=value_input_option, body=body).execute()
            print(f"{result.get('updatedCells')} cells updated.")
            return result
        except HttpError as error:
            print(f"An error occurred: {error}")
            return error


def main():
    gsi = GoogleApi()
    test_rows = 'List1!F4:G6'
    test_values = [
        ['Test11', 12],
        ['Test12', 22],
        ['Test13', 32]
    ]
    # gsi.update_title(title="Test")
    gsi.get_rows(range='Лист3')
    gsi.updated_rows(rows=test_rows, values=test_values)


if __name__ == '__main__':
    main()