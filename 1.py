import classes

class Student(classes.Human):
    print("Hello")
    def __init__(self, name, money, height):
        self.name = name
        self.money = money
        self.height = height
        print("Init") 
    def BuyPizza(self):
        self.money -= 100 
        print(self.name, "bought a pizza. Now you have", self.money, "uah")

class Car:
    def __init__(self):
        self.color = "red"
        self.model = "BMW"


s = Student('Alex', 200, 180)
s2 = Student("Renat", 300, 190)
car = Car()
print(car.color, car.model)
s.money = 200
print(s.name,s.money, s2.name, s2.money)
s.BuyPizza()
s.jump()

class Test(classes.Human):
    pass

test = Test()
print(test.name, test.height)