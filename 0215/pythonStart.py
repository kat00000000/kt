class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email


Taro = Person("Taro", "Taro@python.com")
Jiro = Person("Jiro", "Jiro@python.com")

Person_info = [Taro, Jiro]

for member in Person_info:
    print("Name:", member.name, " Email:", member.email)