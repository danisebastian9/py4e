wordWithoutVowels = ""
userWord = input("Enter your word: ")
userWord = userWord.upper()

for letter in userWord:
    if letter == "A":
        letter += wordWithoutVowels
        Continue

    # Complete the body of the loop.
print(wordWithoutVowels)
# Print the word assigned to wordWithoutVowels.
