import gspread
from google.oauth2.service_account import Credentials
from prettytable import PrettyTable
from datetime import datetime   # import for printing time
import time,os,sys


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("burger_lab")

burger = SHEET.worksheet("burger")
doneness = SHEET.worksheet("doneness")
toppings = SHEET.worksheet("toppings")
drink = SHEET.worksheet("drink")


customer_order = []
selected_doneness = []
selected_toppings = []
meal_deal = []
price = []



def print_type(text):
    """
    Python Typing Text Effect form
    www.101computing.net/python-typing-text-effect/
    """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


def input_type(text):
    """
    code from www.101computing.net/python-typing-text-effect/
    """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()
    return value


def clearScreen():
    """
    Clear screen effect.
    """
    os.system("clear")


def buffer():
    """
    Pause after warning before clearing screen
    """
    time.sleep(.5)


# x = PrettyTable()

# data = burger.get_all_values()
# x.field_names = ["Burger Type"]
# x.add_row([f"type: {data}"])

# print(x)

