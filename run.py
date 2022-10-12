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
toppings = SHEET.worksheet("toppings").get_all_values()
top_list = toppings
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


def get_order():
    """
    Get order info from user,
    which type of burger.
    """
    print_type("Hello & welcome to Burger Lab.\n")
    print_type("What type of burger can I get you today?\n")
    print_type("You can select from Beef or Vegan.\n")
    # Request user input
    type_of_burger = input_type("Please enter Beef or Vegan.\n")
    if type_of_burger.lower() == ("beef"):
        print_type("\nGreat! You have chosen a Beef burger.\n")
        customer_order.append("Beef burger.")
        # return type_of_burger
    elif type_of_burger.lower() == ("vegan"):
        print_type("\nExcellent! You have chosen a Vegan burger.\n")
        customer_order.append("Vegan burger.")
        # return type_of_burger
    else:
    # elif type_of_burger.lower() != ("b", "v"):
        print_type("Oops. Looks like you choose something that's not available. Should we try this again.\n")
        # Function that calls a pause before clearing the screen
        buffer()
        clearScreen()
        get_order()


def update_worksheet(data, worksheet):
    """
    Receives user burger type to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    


def get_toppings():
    toppings_list = []
    print_type("\nWhat toppings would you like for your burger?\n")
    for type in top_list:
        toppings_list.append(type)
    num = []  
    for i in range(1, 9):
        num.append(i)

    get_toppings.type = dict(zip(num, toppings_list))
    type_table = PrettyTable()
    type_table.field_names = num
    type_table.add_row(toppings)
    print(type_table)
    





def main():
    """
    Run all program funcions
    """
    get_order()
    get_toppings()
    update_worksheet(customer_order, "receipt")
    # print(customer_order)
main()
