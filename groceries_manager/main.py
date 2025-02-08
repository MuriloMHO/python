products = [] #keep track of all the inputed products
total = 0 #keep track of the total amount to pay for the products

def config(): #select from a list of options and run their functions
    print("""
Products Manager:\n
1 to add items:
2 to delete items:
3 to display list:
4 to search:
5 to sort list:
6 to reverse list:
7 to exit:
""")
    
    try: #get user input and run its respective function, if none of them match, display an error message and run the manager again
        prompt = int(input("Type here: "))
        if prompt == 1:
            add_items()

        elif prompt == 2:
            del_items()

        elif prompt == 3:
            display_list()

        elif prompt == 4:
            search_items()

        elif prompt == 5:
            sort_items()

        elif prompt == 6:
            reverse_items()

        elif prompt == 7:
            exit()

        else:
            print("Enter a valid input: ")
            config()

    except ValueError: #prints a error messange if no int value is inputed and run the manager again
        print("Enter a valid input: ")
        config()

def add_items():
    """function to add itens to products list"""
    while True: #keep the add function in loop
        items = input("\nEnter the item you want to add to the list, its price and the desired quantity (ex: Milk, 2.00, 1). To go back to the Product Manager enter '1': ") #get product, price and quantity from user and ask if it want to go back to the manager

        if items == "1": #control if the program is gonna go back to manager or not
            config()

        formating_1 = items.split(",") #divide the string input in itens add it to a list
        if len(formating_1) != 3:
            print("Please provide item, price, and quantity.")
            continue  # Ask for input again if format is incorrect
        
        item_info = [item.strip() for item in formating_1] #remove spaces for all list items and add to a new variable

        try:
            # Convert price and quantity, calculate total
            item_name = item_info[0].title()
            price = float(item_info[1])
            quantity = int(item_info[2])

            # Validate price and quantity
            if price <= 0 or quantity <= 0:
                print("Price and quantity must be greater than zero. Please try again.")
                continue  # Retry if values are invalid
            
            # Calculate total price for the item
            total_price = price * quantity

            # Append item info as a tuple to products
            products.append((item_name, price, quantity, total_price))

            # Recalculate the total for all items
            total_to_pay()

            # Display updated products list
            for items in products:
                print(f"Item: {items[0]}, Price: £{items[1]:.2f}, Quantity: {items[2]}, Total: £{items[3]:.2f}.")
            print(f"\nTotal to pay for all items: £{total:.2f}.\n")

            continue #keep looping to add new items

        except ValueError: #if none of the requirement above are meet, print an error message and ask for another input
            print("Invalid input. Price and quantity must be numbers.")
            continue 

def del_items():
    """Delete products and their information from the list based on their name"""

    item_name = input("Enter the name of the item to delete: ") #ask the item user want to delete
    global products
    found = False
    for i, item in enumerate(products):
        if item[0] == item_name.title():
            del products[i]
            found = True
            break

    if not found: #let user know if the product wasn't find
        print(f"Item '{item_name}' not found.")
    total_to_pay() #update total amount to pay
    display_list() #display list, total amount to pay and run Product Manager

def display_list():
    """display list, total amount to pay and run Product Manager"""
    for items in products:
        print(f"Item: {items[0]}, Price: £{items[1]:.2f}, Quantity: {items[2]}, Total: £{items[3]:.2f}.")
    print(f"\nTotal to pay for all items: £{total:.2f}.")
    config()

def search_items():
    """search and display asked product as well as its information"""
    search = input("\nEnter item's name: ").title() #ask user for the product it wants to find
    found = False
    for items in products:
        if search == items[0]:
            print(f"Item: {items[0]}, Price: £{items[1]:.2f}, Quantity: {items[2]}, Total: £{items[3]:.2f}.")
            found = True
            break

    if not found: #let user know if the product couldn't be find and run Product Manager
        print(f"\nSorry, {search} not found.")
    config()

def sort_items():
    """sort list in alphabetic order permanently"""
    products.sort()
    print("\nList sorted.")
    display_list() #display list, total amount to pay and run Product Manager

def reverse_items():
    """reverse the order of the items"""
    products.reverse()
    print("\nList reversed.")
    display_list() #display list, total amount to pay and run Product Manager

def total_to_pay():
    """calculate total amount to pay"""
    global total
    total = sum(item[3] for item in products)

config()