def sort_key(dict):
    return dict["num"] 

with open("books/frankenstein.txt") as f:
    file_contents = f.read()

words = len(file_contents.split())

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

# print(letters)
list_letters.sort(reverse=True, key=sort_key)
for i in list_letters:
    print(f"The '{i["letter"]}' character was found {i["num"]} times")
print("--- End report ---")
