import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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
    Get dailysales figures input from the user
    """
    while True:
        print("Kindly provide sales data from yesterday's sales.")
        print("Data should be twelve numbers, separated by commas.")
        print("Example: 10,15,20,25,30,35,40,45,50,55,60,65\n")

        data_str = input("Enter your data here: ")
        dailysales_data = data_str.split(",")

        if validate_data(dailysales_data):
            print("Valid data!")
            break

    return dailysales_data


def validate_data(values):
    """
    Covert string values to integer.
    Display error if string values cannot be convert into integer.
    or if the values are below or above twelve
    """
    try:
        [int(value) for value in values]
        if len(values) != 12:
            raise ValueError(
               f"Only 12 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, try again.\n")
        return False

    return True


def update_worksheet(data, worksheet):
    """
    Receive a list of integers to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet update successfully\n")


def calculate_leftover_data(dailysales_row):
    """
    Calculate dailysales with leftover for ice cream
    """
    print("Calculate leftove data...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]

    leftove_data = []
    for stock, dailysales in zip(stock_row, dailysales_row):
        leftove = int(stock) - dailysales
        leftove_data.append(leftove)

    return leftove_data


def main():
    """
    Run all program function
    """
    data = get_dailysales_data()
    dailysales_data = [int(num) for num in data]
    update_worksheet(dailysales_data, "dailysales")
    new_leftover_data = calculate_leftover_data(dailysales_data)
    update_worksheet(new_leftover_data, "leftover")


print("Welcome to Sweet Freeze Data Automation")
main()
