import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('sweet_freeze')

def get_dailysales_data():
    """
    Get dailysales input from customers
    """

    print("Provide dailysales data from the last market day.")
    print("Data should be twelve numbers, separated by commas.")
    print("10,15,22,30,36,42,50,56,60,70,90,98\n")

    data_str = input("Enter your data here: ")
    

    dailysales_data = data_str.split(',')
    print(dailysales_data)

get_dailysales_data()

