# For Loops
# 1. Consider the following furniture: table, chair, cabinet, desk, couch
# 2. Set all the furniture in the variable named "furniture"
# 3. Next, use the continue statement and make x equal to "cabinet"
# 4. Use the print() function to print them in a list
#
# While Loops
# 1. Set i to be equal to 1
# 2. Use the print() function to print i while it is less than 15
# 3. Increment the variable by 1 so it doesn't go on forever
# 4. Then, use the else keyword to print "i is no longer less than 15"


#For Loop

furniture = ["table", "chair", "cabinet", "desk", "couch"]

for x in furniture:
    if x == "cabinet":
        continue
    print(x)

#While Loops

i = 1
while i < 15:
    print(i)
    i += 1
else:
    print("i is no longer less than 15.")