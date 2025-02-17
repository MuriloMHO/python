class Restaurant:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_rest(self):
        print(f"\nThe restaurant name is {self.name}, and it is a {self.type} restaurant.")

    def open_rest(self):
        print(f"The restaurant {self.name} is now open!")

rest = Restaurant("Mammia", "italian")
rest_2 = Restaurant("Mc Donalds", "american")
rest_3 = Restaurant("Burgur King", "american")

rest.describe_rest()
rest.open_rest()

rest_2.describe_rest()
rest_2.open_rest()

rest_3.describe_rest()
rest_3.open_rest()