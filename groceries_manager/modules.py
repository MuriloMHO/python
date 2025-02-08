def formated_items(groceries):
    items_list = groceries.split(",")
    global new_list
    new_list = []

    for items in items_list:
        new_list.append(items.strip())
    
    return new_list

def items_price():
    item_final_price = int(new_list[1]) * int(new_list[2])
    return item_final_price
