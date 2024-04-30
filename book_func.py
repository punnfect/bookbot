import re

# used for return_letter_totals func
def sort_key(dict):
    return dict["num"]

# Prints out number of letters used in decending order
def return_letter_totals(file_contents):
    list_letters = []
    letters = {}
    for i in file_contents:
        i = i.lower()
        if i.isalpha():
            if i not in letters:
                letters[i] =  1
            else:
                letters[i] += 1

    for i in letters:
        list_letters.append({"letter": i, "num": letters[i]})

    list_letters.sort(reverse=True, key=sort_key)

    for i in list_letters:
        print(f"The '{i["letter"]}' character was found {i["num"]} times")
    print("--- End report ---")

# find the amount of times a specific word or name was written - case sensitive and insensitive
def find_word(file_contents, book):
    find = input("What word would you like to find? \n")
    
    while True:
        case_sensitive = input("Case sensitive Y/N: ").lower()
        if case_sensitive == "y":
            words = re.findall(rf"\W?{find}[\W?]s?", file_contents)
            break
        elif case_sensitive == "n":
            words = re.findall(rf"\W?{find}[\W?]s?", file_contents, flags=re.IGNORECASE)
            break
        else:
            print("Usage: Type 'Y' or 'N'")
    print(f"There are {len(words)} occurrences of the word '{find}' in {book}")


