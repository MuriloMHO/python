groceries = []
total = 0

def config():
    print("""
Grocery Manager:\n
1 to add items:
2 to delete items:
3 to display list:
4 to search:
5 to sort list:
6 to reverse list:
7 to exit:
""")
    
    try:
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

    except ValueError:
        print("Enter a valid input: ")
        config()

def add_items():
    while True:
        items = input("\nEnter the item you want to add to the list, its price and the desired quantity (ex: Milk, 2.00, 1). To go back to the Grocery Manager enter '1': ")
        if items == "1":
            config()

        formating_1 = items.split(",")
        if len(formating_1) != 3:
            print("Please provide item, price, and quantity.")
            continue  # Ask for input again if format is incorrect
        
        item_info = [item.strip() for item in formating_1]

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

            # Append item info as a tuple to groceries
            groceries.append((item_name, price, quantity, total_price))

            # Recalculate the total for all items
            total_to_pay()

            # Display updated groceries list
            for items in groceries:
                print(f"Item: {items[0]}, Price: £{items[1]:.2f}, Quantity: {items[2]}, Total: £{items[3]:.2f}.")
            print(f"\nTotal to pay for all items: £{total:.2f}.\n")

            continue

        except ValueError:
            print("Invalid input. Price and quantity must be numbers.")
            continue 

def del_items():
    item_name = input("Enter the name of the item to delete: ")
    global groceries
    found = False
    for i, item in enumerate(groceries):
        if item[0] == item_name.title():
            del groceries[i]
            found = True
            break
    if not found:
        print(f"Item '{item_name}' not found.")
    total_to_pay()
    display_list()

def display_list():
    for items in groceries:
        print(f"Item: {items[0]}, Price: £{items[1]:.2f}, Quantity: {items[2]}, Total: £{items[3]:.2f}.")
    print(f"\nTotal to pay for all items: £{total:.2f}.")
    config()

def search_items():
    search = input("\nEnter item's name: ").title()
    found = False
    for items in groceries:
        if search == items[0]:
            print(f"Item: {items[0]}, Price: £{items[1]:.2f}, Quantity: {items[2]}, Total: £{items[3]:.2f}.")
            found = True
            break
    if not found:
        print(f"\nSorry, {search} not found.")
    config()

def sort_items():
    groceries.sort()
    print("\nList sorted.")
    display_list()

def reverse_items():
    groceries.reverse()
    print("\nList reversed.")
    display_list()

def total_to_pay():
    global total
    total = sum(item[3] for item in groceries)

config()