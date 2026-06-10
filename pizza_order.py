import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import os

# BASE CLASS

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

# PIZZA CLASSES (INHERITANCE)

class Pizza(MenuItem):
    pass


class VegetarianPizza(Pizza):
    def get_price(self):
        return self.price


class MeatPizza(Pizza):
    def get_price(self):
        return self.price + 1.50


class SeafoodPizza(Pizza):
    def get_price(self):
        return self.price + 2.00

# TOPPINGS & SIDES

class Topping(MenuItem):
    pass


class SideOrder(MenuItem):
    pass

# CUSTOMER

class Customer:
    def __init__(self, name):
        self.name = name

# ORDER

class Order:

    order_counter = 1

    def __init__(self):
        self.order_number = Order.order_counter
        Order.order_counter += 1

        self.customer = None
        self.pizza = None
        self.size = "Small"
        self.toppings = []
        self.sides = []
        self.timestamp = datetime.now()

    def calculate_total(self):

        total = self.pizza.get_price()

        size_prices = {
            "Small": 0,
            "Medium": 2,
            "Large": 4
        }

        total += size_prices[self.size]

        for topping in self.toppings:
            total += topping.get_price()

        for side in self.sides:
            total += side.get_price()

        return total

    def generate_receipt(self):

        receipt = []
        receipt.append("=" * 40)
        receipt.append("YOUR WAY PIZZA PARLOUR")
        receipt.append("=" * 40)

        receipt.append(f"Order Number: {self.order_number}")
        receipt.append(f"Date: {self.timestamp.strftime('%d/%m/%Y %H:%M:%S')}")

        receipt.append("")
        receipt.append(f"Customer: {self.customer.name}")

        receipt.append("")
        receipt.append("PIZZA")
        receipt.append(f"{self.pizza.name} ({self.size})")

        receipt.append("")
        receipt.append("TOPPINGS")

        if self.toppings:
            for topping in self.toppings:
                receipt.append(
                    f"{topping.name} - £{topping.get_price():.2f}"
                )
        else:
            receipt.append("None")

        receipt.append("")
        receipt.append("SIDES")

        if self.sides:
            for side in self.sides:
                receipt.append(
                    f"{side.name} - £{side.get_price():.2f}"
                )
        else:
            receipt.append("None")

        receipt.append("")
        receipt.append(
            f"TOTAL: £{self.calculate_total():.2f}"
        )

        receipt.append("")
        receipt.append("Thank you for your order!")

        return "\n".join(receipt)

    def save_receipt(self):

        os.makedirs("receipts", exist_ok=True)

        filename = (
            f"receipts/receipt_{self.order_number}.txt"
        )

        with open(filename, "w") as file:
            file.write(self.generate_receipt())

    def send_to_chef(self):

        with open("chef_orders.txt", "a") as file:
            file.write(self.generate_receipt())
            file.write("\n\n")

# GUI

class PizzaApp:

    def __init__(self, root):

        self.root = root
        self.root.title("Your Way Pizza Parlour")
        self.root.geometry("900x700")

        self.create_menu_data()
        self.create_widgets()

    # ----------------------------------------------

    def create_menu_data(self):

        self.pizzas = {
            "Margherita":
                Pizza("Margherita", 8),

            "Vegetarian":
                VegetarianPizza("Vegetarian", 9),

            "Pepperoni":
                MeatPizza("Pepperoni", 10),

            "Meat Feast":
                MeatPizza("Meat Feast", 11),

            "Seafood Deluxe":
                SeafoodPizza("Seafood Deluxe", 12)
        }

        self.topping_items = {
            "Extra Cheese": Topping("Extra Cheese", 1),
            "Mushrooms": Topping("Mushrooms", 1),
            "Peppers": Topping("Peppers", 1),
            "Onions": Topping("Onions", 1),
            "Jalapenos": Topping("Jalapenos", 1.5),
            "Bacon": Topping("Bacon", 2)
        }

        self.side_items = {
            "Garlic Bread": SideOrder("Garlic Bread", 3),
            "Fries": SideOrder("Fries", 2.5),
            "Chicken Wings": SideOrder("Chicken Wings", 4),
            "Mozzarella Sticks": SideOrder("Mozzarella Sticks", 3.5)
        }

    # ----------------------------------------------

    def create_widgets(self):

        title = tk.Label(
            self.root,
            text="YOUR WAY PIZZA PARLOUR",
            font=("Arial", 18, "bold")
        )
        title.pack(pady=10)

        main_frame = tk.Frame(self.root)
        main_frame.pack(fill="both", expand=True)

        left_frame = tk.Frame(main_frame)
        left_frame.pack(side="left", padx=20)

        right_frame = tk.Frame(main_frame)
        right_frame.pack(side="right", padx=20)

        # CUSTOMER

        tk.Label(
            left_frame,
            text="Customer Name"
        ).pack()

        self.customer_entry = tk.Entry(
            left_frame,
            width=30
        )
        self.customer_entry.pack(pady=5)

        # PIZZA

        tk.Label(
            left_frame,
            text="Choose Pizza"
        ).pack()

        self.pizza_var = tk.StringVar()

        self.pizza_combo = ttk.Combobox(
            left_frame,
            textvariable=self.pizza_var,
            values=list(self.pizzas.keys()),
            state="readonly"
        )

        self.pizza_combo.pack()

        # SIZE

        tk.Label(
            left_frame,
            text="Size"
        ).pack(pady=10)

        self.size_var = tk.StringVar(
            value="Small"
        )

        for size in ["Small", "Medium", "Large"]:
            tk.Radiobutton(
                left_frame,
                text=size,
                variable=self.size_var,
                value=size,
                command=self.update_summary
            ).pack(anchor="w")

        # TOPPINGS

        tk.Label(
            left_frame,
            text="Extra Toppings"
        ).pack(pady=10)

        self.topping_vars = {}

        for topping in self.topping_items:

            var = tk.BooleanVar()

            self.topping_vars[topping] = var

            tk.Checkbutton(
                left_frame,
                text=f"{topping}",
                variable=var,
                command=self.update_summary
            ).pack(anchor="w")

        # SIDES

        tk.Label(
            left_frame,
            text="Side Orders"
        ).pack(pady=10)

        self.side_vars = {}

        for side in self.side_items:

            var = tk.BooleanVar()

            self.side_vars[side] = var

            tk.Checkbutton(
                left_frame,
                text=f"{side}",
                variable=var,
                command=self.update_summary
            ).pack(anchor="w")

        # SUMMARY PANEL

        tk.Label(
            right_frame,
            text="ORDER SUMMARY",
            font=("Arial", 14, "bold")
        ).pack()

        self.summary_box = tk.Text(
            right_frame,
            width=40,
            height=25
        )

        self.summary_box.pack()

        self.total_label = tk.Label(
            right_frame,
            text="TOTAL: £0.00",
            font=("Arial", 14, "bold")
        )

        self.total_label.pack(pady=10)

        tk.Button(
            right_frame,
            text="Update Order",
            command=self.update_summary
        ).pack(fill="x")

        tk.Button(
            right_frame,
            text="Submit Order",
            command=self.submit_order
        ).pack(fill="x", pady=5)

    # ----------------------------------------------

    def build_order(self):

        order = Order()

        customer_name = self.customer_entry.get().strip()

        order.customer = Customer(customer_name)

        order.pizza = self.pizzas[
            self.pizza_var.get()
        ]

        order.size = self.size_var.get()

        for topping, var in self.topping_vars.items():

            if var.get():
                order.toppings.append(
                    self.topping_items[topping]
                )

        for side, var in self.side_vars.items():

            if var.get():
                order.sides.append(
                    self.side_items[side]
                )

        return order

    # ----------------------------------------------

    def update_summary(self):

        if not self.pizza_var.get():
            return

        order = self.build_order()

        self.summary_box.delete(
            "1.0",
            tk.END
        )

        self.summary_box.insert(
            tk.END,
            f"Pizza: {order.pizza.name}\n"
        )

        self.summary_box.insert(
            tk.END,
            f"Size: {order.size}\n\n"
        )

        self.summary_box.insert(
            tk.END,
            "Toppings:\n"
        )

        for topping in order.toppings:
            self.summary_box.insert(
                tk.END,
                f"- {topping.name}\n"
            )

        self.summary_box.insert(
            tk.END,
            "\nSides:\n"
        )

        for side in order.sides:
            self.summary_box.insert(
                tk.END,
                f"- {side.name}\n"
            )

        self.total_label.config(
            text=f"TOTAL: £{order.calculate_total():.2f}"
        )

    # ----------------------------------------------

    def submit_order(self):

        if self.customer_entry.get().strip() == "":
            messagebox.showerror(
                "Validation Error",
                "Please enter your name."
            )
            return

        if self.pizza_var.get() == "":
            messagebox.showerror(
                "Validation Error",
                "Please choose a pizza."
            )
            return

        order = self.build_order()

        order.send_to_chef()
        order.save_receipt()

        self.show_bill(order)

    # ----------------------------------------------

    def show_bill(self, order):

        bill_window = tk.Toplevel(self.root)

        bill_window.title(
            f"Receipt #{order.order_number}"
        )

        text = tk.Text(
            bill_window,
            width=50,
            height=30
        )

        text.pack()

        text.insert(
            tk.END,
            order.generate_receipt()
        )

        text.config(state="disabled")

# MAIN

root = tk.Tk()
app = PizzaApp(root)
root.mainloop()