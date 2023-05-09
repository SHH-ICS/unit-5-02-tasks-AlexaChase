# Create a program that will accept a word from a user and return the length of that word.
# Make this program in a loop with option to exit when the use types in quit.
word= str()
while word != "quit":
    word= input("Please enter a word:")
    print("The length of the word is", len(word), "characters long")
print ("Have a great day!")
