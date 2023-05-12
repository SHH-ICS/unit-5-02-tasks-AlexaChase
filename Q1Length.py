# Create a program that will accept a word from a user and return the length of that word.
# Make this program in a loop with option to exit when the use types in quit.
word= str()
word= input("Please enter a word:")
while word != "quit":
    print("The length of the word is", len(word), "characters long")
    word= input("Please enter a word:")
print ("Have a great day!")
