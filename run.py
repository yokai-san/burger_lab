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
top_list = toppings.col_values(1)[1:]
drink = SHEET.worksheet("drink")


CUSTOMER_ORDER = []
# selected_doneness = []
SELECTED_TOPPINGS = []
TOPPING_CHOICE = []
# price = []



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


now = datetime.now()
date_stamp = now.strftime("%a:%d:%b:%y")
time_stamp = now.strftime("%H:%M")


# x = PrettyTable()

# data = burger.get_all_values()
# x.field_names = ["Burger Type"]
# x.add_row([f"type: {data}"])

# print(x)


print("""\
    
  ____                                 
 | __ ) _   _ _ __ __ _  ___ _ __      
 |  _ \| | | | '__/ _` |/ _ \ '__|     
 | |_) | |_| | | | (_| |  __/ |        
 |____/ \__,_|_|  \__, |\___|_|        
                  |___/          _     
                     | |    __ _| |__  
                     | |   / _` | '_ \ 
                     | |__| (_| | |_) |
                     |_____\__,_|_.__/ 
                                       
                                       
                                       """)

def get_order():
    """
    Get order info from user,
    which type of burger.
    """
    print_type("Hello & welcome to Burger Lab.\n")
    print_type("\nWhat type of burger can I get you today?\n")
    print_type("You can select from Beef or Vegan.\n")
    # Request user input
    type_of_burger = input_type("\nPlease enter Beef or Vegan:\n")
    if type_of_burger.lower() == ("beef"):
        print_type("\nGreat! You have chosen a Beef burger.\n")
        CUSTOMER_ORDER.append("Beef burger.")
        # return type_of_burger
    elif type_of_burger.lower() == ("vegan"):
        print_type("\nExcellent! You have chosen a Vegan burger.\n")
        CUSTOMER_ORDER.append("Vegan burger.")
        # return type_of_burger
    else:
    # elif type_of_burger.lower() != ("b", "v"):
        print_type("Oops. Looks like you choose something that's not available. Should we try this again.\n")
        # Function that calls a pause before clearing the screen
        buffer()
        clearScreen()
        get_order()


def get_cheese():
    """
    Ask user if they want cheese on burger.
    """
    print_type("\nWould you like cheese on your burger?\n")
    cheese_on_burger = input_type("y/n:\n")
    if cheese_on_burger.lower() == ("y"):
        print_type("\nYou have added cheese to your to burger.\n")
        CUSTOMER_ORDER.append("Cheese")

def update_worksheet(data, worksheet):
    """
    Receives user burger type to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)


def getting_toppings_list():
    global TOPPING_CHOICE
    print_type("\nWhat toppings would you like for your burger?\n")

    toppings = ["Pickle", "Onion", "Lettuce", "Tomato", "Ketchep", "Mustard", "Mayo"]
    for count, value in enumerate(toppings, start=1):
        print('{} - {}'.format(count, value))

    choice = int(input("Please enter toppings by numbers: "))
    
    TOPPING_CHOICE.append(toppings[choice-1])
    print_type(f"\nYou have added {TOPPING_CHOICE} to your burger.\n")
    CUSTOMER_ORDER.append(TOPPING_CHOICE)
    buffer()
    clearScreen()
    

    
# def get_toppings_table():
#     """
#     Pulling toppings list from Google Worksheet and
#     Saving it in a variable so that it can be used in
#     prettytable function.
#     """
#     toppings_list = []
#     print_type("\nWhat toppings would you like for your burger?\n")
#     for type in top_list:
#         toppings_list.append(type)
#     num = []  
#     for i in range(1, 7):
#         num.append(i)

#     get_toppings_table.type = dict(zip(num, toppings_list))
#     type_table = PrettyTable()
#     type_table.field_names = num
#     type_table.add_row(toppings_list)
#     print(type_table)

# def get_toppings():
#     global SELECTED_TOPPINGS
#     tops = []
#     (map(int, input_type("\nPlease select toppings by using corresponding number:\n")))
#     SELECTED_TOPPINGS = [int(i)for i in tops]

#     # return SELECTED_TOPPINGS
#     CUSTOMER_ORDER.append(SELECTED_TOPPINGS)
#     get_toppings_choice()



# def get_toppings_choice():
#     global TOPPING_CHOICE
#     TOPPING_CHOICE = []
#     for x in SELECTED_TOPPINGS:
#         TOPPING_CHOICE.append(top_list[x - 1])


def print_order():
    """
    Print order with prettytable
    """
    receipt = PrettyTable()
    receipt.field_names = (["**Your burger!**"])
    receipt.add_row([f'Date: {date_stamp}'])
    receipt.add_row([f'Time: {time_stamp}'])
    receipt.add_row([f"Order: {CUSTOMER_ORDER}"])
    print(receipt)

def good_bye():
    print("""\
   _____ _                 _                       
  |_   _| |__   __ _ _ __ | | __                   
    | | | '_ \ / _` | '_ \| |/ /                   
    | | | | | | (_| | | | |   <                    
    |_| |_| |_|\__,_|_| |_|_|\_\                   
       | | | |/ _ \| | | |                         
       | |_| | (_) | |_| |                         
   __   \__, |\___/ \__,_|     _ _   _             
  / _| _|___/ __  __   _(_)___(_) |_(_)_ __   __ _ 
 | |_ / _ \| '__| \ \ / / / __| | __| | '_ \ / _` |
 |  _| (_) | |     \ V /| \__ \ | |_| | | | | (_| |
 |_|  \___/|_|      \_/ |_|___/_|\__|_|_| |_|\__, |
     | __ ) _   _ _ __ __ _  ___ _ __        |___/ 
     |  _ \| | | | '__/ _` |/ _ \ '__|             
     | |_) | |_| | | | (_| |  __/ |                
     |____/ \__,_|_| _\__, |\___|_|                
         | |    __ _| |___/                        
         | |   / _` | '_ \                         
         | |__| (_| | |_) |                        
         |_____\__,_|_.__/                         
                        """)


def main():
    """
    Run all program funcions
    """
    get_order()
    get_cheese()
    getting_toppings_list()
    print_order()
    good_bye()
    # get_toppings_table()
    # get_toppings()
    # get_toppings_choice()
    # update_worksheet(CUSTOMER_ORDER, "receipt")
    # print(CUSTOMER_ORDER)
    # print(TOPPING_CHOICE)


main()


