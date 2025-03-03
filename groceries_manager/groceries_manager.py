# import area

import json
import urllib.parse
import webbrowser

# keep track of important data

products = []
total = 0

# select from a list of options and run their functions

def config(): 
    print("""
Products Manager:\n
1 to add items:
2 to delete items:
3 to clear list:
4 to display list:
5 to search:
6 to sort list:
7 to reverse list:
8 to send to whatsapp:
9 to exit:
""")
    
    try:
        prompt = int(input("Type here: \n"))
        
        if prompt == 1:
            add_items()

        elif prompt == 2:
            del_items()

        elif prompt == 3:
            clear_products()

        elif prompt == 4:
            display_list()

        elif prompt == 5:
            search_items()

        elif prompt == 6:
            sort_items()

        elif prompt == 7:
            reverse_items()

        elif prompt == 8:
            send_whatsapp()

        elif prompt == 9:
            exit()

        else:
            print("Enter a valid input: ")
            config()

    except ValueError:
        print("Enter a valid input: ")
        config()

# add items and their info to the variables at the beggining of the program.

def add_items():
    """function to add itens to products list"""
    while True:

        # get users input for item, price and quanity
        
        items = input("\nEnter the item you want to add to the list, its price and the desired quantity (ex: Milk, 2.00, 1). To go back to the Products Manager enter '1': ")
        items += "" 

        # check if user wants to go back to Product Manager (config)

        if items == "1":
            config()

        # convert string input to fornats that the program will use

        formating_1 = items.split(",")
        if len(formating_1) != 3:
            print("Please provide item, price, and quantity.")
            continue
        
        item_info = [item.strip() for item in formating_1]

        # check if all information the user inputed was filled in properly

        try:
            # all needed variables from inside the function
            
            item_name = item_info[0].title()
            price = float(item_info[1])
            quantity = int(item_info[2])

            # here stars to check the input and run the necessary process to add items and add everything needed

            if price <= 0 or quantity <= 0:
                print("Price and quantity must be greater than zero. Please try again.")
                continue
            
            total_price = price * quantity
            products.append((item_name, price, quantity, total_price))

            # call for necessary functions
            
            total_to_pay()
            save_to_json()
            save_to_json_2()

            # display updated products list
            
            for items in products:
                print(f"Item: {items[0]}, Price: £{items[1]:.2f}, Quantity: {items[2]}, Total: £{items[3]:.2f}.")
            print(f"\nTotal to pay for all items: £{total:.2f}.\n")

            # keep looping to add new items

            continue 

        # if none of the requirement above were meet, print an error message and ask for another input

        except ValueError: 
            print("Invalid input. Price and quantity must be numbers.")
            continue 

# ask the item user want to delete

def del_items():
    """Delete products and their information from the list based on their name"""

    item_name = input("Enter the name of the item to delete: ")
    
    global products
    found = False
    for i, item in enumerate(products):
        if item[0] == item_name.title():
            del products[i]
            found = True
            break

    if not found:
        print(f"Item '{item_name}' not found.")

    # call for necessary functions
    
    total_to_pay()
    save_to_json()
    save_to_json_2()
    display_list()

def clear_products():
    """Clear all items in the list"""
    
    products.clear()
    total_to_pay()
    display_list()

def display_list():
    """display list, total amount to pay and run Product Manager"""
    
    for items in products:
        print(f"Item: {items[0]}, Price: £{items[1]:.2f}, Quantity: {items[2]}, Total: £{items[3]:.2f}.")
    print(f"\nTotal to pay for all items: £{total:.2f}.")
    config()

def search_items():
    """search and display asked product as well as its information"""
    
    search = input("\nEnter item's name: ").title()
    found = False
    for items in products:
        if search == items[0]:
            print(f"Item: {items[0]}, Price: £{items[1]:.2f}, Quantity: {items[2]}, Total: £{items[3]:.2f}.")
            found = True
            break

    if not found:
        print(f"\nSorry, {search} not found.")
    config()

def sort_items():
    """sort list in alphabetic order permanently"""
    
    products.sort()
    print("\nList sorted.")

    # call for necessary functions
    
    save_to_json()
    save_to_json_2()
    display_list()

def reverse_items():
    """reverse the order of the items"""
    products.reverse()
    print("\nList reversed.")

    # call for necessary functions
    
    save_to_json()
    save_to_json_2()
    display_list()

def total_to_pay():
    """calculate total amount to pay"""
    
    global total
    total = sum(item[3] for item in products)

def save_to_json():
    """save the variable 'products' to  a JSSON file"""
    
    with open("product.json", "w") as file:
        json.dump(products, file, indent = 4)

def save_to_json_2():
    """save the variable 'total' to  a JSSON file"""
    
    with open("total.json", "w") as file:
        json.dump(total, file, indent = 4)

def load_from_json():
    """load information of the variable 'products' from the JSON file"""
    
    global products
    try:
        with open("product.json", "r") as file:
            products = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        products = []

def load_from_json_2():
    """load information of the variable 'products' from the JSON file"""
    
    global total
    try:
        with open("total.json", "r") as file:
            total = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        total = []

def send_whatsapp():
    """send products list to WhatsApp via a pre-filled message link"""
    
    if not products:
        print("No products to send.")
        config()

    # format the products into a readable message
    message = "🛒 *Shopping List:*\n"
    for item in products:
        message += f"✅ {item[0]} - £{item[1]:.2f} x {item[2]} = £{item[3]:.2f}\n"
    
    message += f"\n💰 *Total: £{total:.2f}*"

    # encode message for URL
    encoded_message = urllib.parse.quote(message)

    # whatsApp link (replace with your number if needed)
    whatsapp_link = f"https://web.whatsapp.com/send?text={encoded_message}"

    # open the link in a web browser
    webbrowser.open(whatsapp_link)
    print("Opening WhatsApp...")

    config()

# get all saved info and starts the program

load_from_json()
load_from_json_2()
config()
