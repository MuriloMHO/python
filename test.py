def formated_items(groceries):
    items_list = groceries.split(",")
    new_list = []

    for items in items_list:
        items = items.strip()
        new_list.append(items)
    
    return new_list

groceries = formated_items(input("Enter an item and its price (Milk, £2): "))

print(groceries)