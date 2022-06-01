class Customers:
    greeting = "Welcome to the Coffee Palace!"

    def __init__(self, name, beverage, food, total):
        self.name = name
        self.beverage = beverage
        self.food = food
        self.total = total


c_1 = Customers("Yuri Cruz", "Coke", "Spaghetti", 95)
c_2 = Customers("Hans Reyes", "Cafe latte", "Custard cake" , 135)


print(Customers.greeting)
print(c_1.name)
print(c_1.beverage)
print(c_1.food)
print(c_1.total)