import glob
import book_functions


while True:
    count = 0
    book_name = input("-------------------Options------------------- \nType the name of the book you're looking for, \nType 'Books' for a list of available books, \nType '.' to cancel program \n")
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
        except FileNotFoundError:
            print(f"'{book_name}' not found in directory. \nExiting program... ")
            exit()

# words = len(file_contents.split())



# book_functions.return_letter_totals(file_contents)


