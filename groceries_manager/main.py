from modules import *

_list = {

}

num_gen = 0
item = []
total = 0
flag = True


while flag:
    def add_items():
        groceries = formated_items(input("\nEnter an item, its price, and desired quantity (ex: Milk, 2, 1). Enter \"q\" to quit: "))

        if groceries == "quit":
            flag = False

        groceries_list = groceries

        if len(groceries_list) > 3 or len(groceries_list) < 1:
            add_items()

        item_final_price = items_price()

        global num_gen
        num_gen += 1

        _key = str(f"item_{num_gen}")
        _list[_key] = (groceries_list[0], groceries_list[1], groceries_list[2], item_final_price)

        for items in _list.items():
            print(f"Here is your lis: \n{items}")
            global item
            item = items

        global total
        total += item[1][3]

        print(f"Total: {total}")

    prompt = input("\nEnter 1 to add a new item: \nEnter 2 to delete an item: \nEnter 3 to quit: \nType Here: ")

    if prompt == "1":
        add_items()

    if prompt == "3":
        break

    if not _list:
        print("\nAdd at least one item.\n")
        add_items()

    if prompt == "2":
        _del = input("\nEnter the item you want to delete from the list (ex: item_1): ")
        total -= _list[_del][3]
        del _list[_del]
        for items in _list.items():
            print(f"\nHere is your list: \n{items}\n")
        print(f"\nTotal: {total}")

