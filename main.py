def sort_key(dict):
    return dict["num"] 

list_letters = []
letters = {}
book_name = input("Name of the book? ")

try:
    with open(f"books/{book_name}.txt") as f:
        file_contents = f.read()
except FileNotFoundError:
    print(f"'{book_name}' not found in directory. \nExiting program... ")
    exit()

words = len(file_contents.split())

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
