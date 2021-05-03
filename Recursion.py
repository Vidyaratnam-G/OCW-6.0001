def first_letter_recursive(word):
    # while word != "":
    if word != "":
        print(word[0])
        word = word[1:]
        first_letter_recursive(word)


first_letter_recursive("Python")
