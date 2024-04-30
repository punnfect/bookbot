import glob
import book_func
import re


while True:
    count = 0
    book_name = input("--------------------Options-------------------- \n\
1. Type the name of the book you're looking for, \n\
2. Type 'Books' for a list of available books, \n\
3. Type '.' to cancel program \n")
    if book_name.lower() == "books":
        # pulls all txt files in books folder 
        files = glob.glob('books/*.txt')
        print(f"There are {len(files)} books in the library.")
        for file in files:
            count += 1
            print(f"{count}. {file[6:-4:]}")
    elif book_name == ".":
        print("Exiting program... ")
        exit()
    else:
        try:
            with open(f"books/{book_name}.txt") as f:
                file_contents = f.read()
                break
        except FileNotFoundError:
            print(f"'{book_name}' not found in directory. \nExiting program... ")
            exit()

while True:
    option_choice = input("--------------------Options-------------------- \n\
1. Type 1 to display each letters total useage in decending order, \n\
2. Type 2 to search how many times a word or phrase are used in the book, \n\
3. Type '.' to cancel program \n")

    match option_choice:
        case "1":
            book_func.return_letter_totals(file_contents)
        case "2":
            book_func.find_word(file_contents, book_name)
        case ".":
            print("Exiting program... ")
            exit()
