# Create a program that will prompt the user for a word, and return a 'word triangle'. For example, if the user types in the word "PYTHON", your program will output:
# P
# PY
# PYT
# PYTH
# PYTHO
# PYTHON
word= str(input("Please enter a word:"))
for l in range(len(word)):
    for w in range(l + 1):
        print(word[w], end="")
    print()
