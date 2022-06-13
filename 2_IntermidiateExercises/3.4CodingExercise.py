# Create a new file. Use the "w' mode.
# Answer the question in one sentence: "What do you like about Python?"
# This time, let's use a "a" mode to add to your file.
#   Answer the following questions:
#       "What do I plan after learning Python?"
#       "How do I apply what I've learned?"
#       "What are my goals?"

myFile = open("exercise3.4.txt", "w")
myFile.write("I like Python because the language easy to learn and understand.")

appendFile = open("exercise3.4.txt", "a")
appendFile.write("\nI will continue learning into advanced uses of Python.")
appendFile.write("\nI want to make a simple app after this.")
appendFile.write("\nI will master this new language to add to my repertoire of skills.")
