def sort_key(dict):
    return dict["num"]

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