class User:
    def __init__(self, f_name, l_name, nickname, age, email):
        self.f_name = f_name
        self.l_name = l_name
        self.nickname = nickname
        self.age = age
        self.email = email

    def describe_user(self):
        print(f"\nThe user called {self.f_name} {self.l_name} is {self.age} years old")
        print(f"The nickname is {self.nickname} and the associated email is {self.email}")

    def greeting_user(self):
        print(f"\nWelcome {self.f_name} {self.l_name}, you are now sucefully logged in as {self.nickname}")

user_1 = User("Murilo", "Machado", "D4KR", 18,"murilomachado@gmail.com")
user_2 = User("Danierlly", "Machado", "Dani", 35,"danierllymachado@gmail.com")
user_3 = User("Erick", "Hoffman", "Hoffman", 39,"erickhoffman@gmail.com")
user_4 = User("Hugo", "Marin", "Marin", 30,"hugomarin@gmail.com")

user_1.describe_user()
user_1.greeting_user()

user_2.describe_user()
user_2.greeting_user()

user_3.describe_user()
user_3.greeting_user()

user_4.describe_user()
user_4.greeting_user()