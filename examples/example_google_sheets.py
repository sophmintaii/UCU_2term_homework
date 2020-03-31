import gspread
from oauth2client.service_account import ServiceAccountCredentials


def get_records():
    # define scope and create credentials using client_secret.json
    # (client_secret.json is a file you get when you enable Google Sheets API)
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('../folder/client_secret.json', scope)
    # create a client who will have access to Google Sheets
    # remember to give to your client email edit rights
    client = gspread.authorize(creds)

    # open first sheet of workbook by name and return records from it
    sheet = client.open('Test form (Responses)').sheet1
    data = sheet.get_all_records()
    return data


if __name__ == "__main__":
    data = get_records()
    print(data)
