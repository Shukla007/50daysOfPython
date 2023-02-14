text = input("Enter some text: ")
count_type = input("Enter 'letter' or 'word' to choose what to count: ")

if count_type == "letter":
    count = len(text)
    print(f"There are {count} letters in text.")

elif count_type == "word":
    word = text.split()
    count = len(word)
    print(f"There are {count} words in the text.")

else:
    print("Invalid count type, plese enter 'letter' ora'word'.")