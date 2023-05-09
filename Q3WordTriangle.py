# Create a program that will prompt the user for a word, and return a 'word triangle'. For example, if the user types in the word "PYTHON", your program will output:
# P
# PY
# PYT
# PYTH
# PYTHO
# PYTHON
word= input("Please enter a word:")
while True:
    print(word[0])
    print(word[0:+1])
