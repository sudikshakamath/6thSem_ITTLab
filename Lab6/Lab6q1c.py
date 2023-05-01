sen = input("Enter a sentence: ")
words = [word.lower() for word in sen.split()]

words.sort()

# display the sorted words

print("The sorted words are:")
for word in words:
    print(word)
