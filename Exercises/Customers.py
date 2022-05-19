# Your new cafe, "Coffee Palace" is an instant hit. Customers are puring in and out every minute!
# So far, you have two regular customers who seem to love buying from your cafe. They show up to eat breakfast
# everyday and they always order the same things.
# Using classes, let's try to save their orders
# 1 Create a class called "Customers"
# 2 Take note of the following information
#  Name         Beverage            Food                Total
#   Samirah     Iced caffe latte   Cinnamon roll       225
#   Jerry       Caramel macchiato   Glazed doughnut     230
# 3 Create a class variable named "greeting", with the value "Welcome to the Coffee Palace!"
# 4 Create instance variables for Samirah and Jerry
# 5 Include the attributes listed on the table
# 6 Type print(Customers.greeting)
# 7 What does Samirah want to drink? Print her beverage on the console
# 8 What does Jerry want to eat? Print his food on the console


class Customers:
    greeting = "Welcome to the Coffee Palace!"

customer1 = Customers()
customer1.name = "Samirah"
customer1.beverage = "Iced caffe latte"
customer1.food = "Cinnamon roll"
customer1.total = 225

customer2 = Customers()
customer2.name = "Jerry"
customer2.beverage = "Caramel macchiato"
customer2.food = "Glazed doughnut"
customer2.total = 230

print(Customers.greeting)
print(customer1.beverage)
print(customer2.food)