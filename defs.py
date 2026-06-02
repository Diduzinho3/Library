book_list = []

def line():
    print("\n---------- // ----------\n")

def create_new_book():

    line()

    book = {
        "ID": int(input("ID: ")),
        "Title": input("Title: ").title(),
        "Author": input("Author: ").title(),
        "Year": int(input("Year: ")),
        "Available": True
    }

    duplicated = False

    for book_ in book_list:

        if book["ID"] != book_["ID"]:
            duplicated = False
        else:
            duplicated = True

    if not duplicated:

        book_list.append(book)

    else: 

        line()

        print("Duplicated ID!")

        create_new_book()

    print("\nBook successfully created!")

    line()

def show_book(book):

    print(f"""
ID: {book["ID"]}
Title: {book["Title"]}
Author: {book["Author"]}
Year: {book["Year"]}
Available: {"Yes" if book["Available"] else "No"}
""")

def show_book_list():

    line()

    if len(book_list) > 0:

        for book in book_list:
            show_book(book)
            line()

    else:
        print("Didn't have any registered book.")
        line()

def search_title():

    title = input("Book Title: ")

    line()

    found = False

    for book in book_list:

        if title.lower() in book["Title"].lower():

            show_book(book)

            found = True

            line()

    if found == False:
        print("Book not found.")
        line()

def remove_by_id(book_id):

    line()

    found = False

    for i, book in enumerate(book_list):

        if book_id == book["ID"]:

            print(book["Title"], "was successfully removed!")

            book_list.pop(i)

            found = True

            line()

            break

    if found == False:
        print("ID not found.")
        line()

def borrow_book(book_id):

    for book in book_list:

        if book_id == book["ID"]:

            if book["Available"]:
                
                line()

                print(f"You sucessfully borrowed {book["Title"]} book!")
                book["Available"] = False

                line()
                
            elif not book["Available"]:

                line()

                print(f"{book["Title"]} cannot be borrowed!")

                line()
            
        else:

            line()

            print("Invalid ID!")

            line()

def return_book(book_id):

    for book in book_list:

        if book_id == book["ID"]:

            if not book["Available"]:
                
                line()

                print(f"{book["Title"]} has returned to library!")
                book["Available"] = True

            elif book["Available"]:
                
                line()

                print(f"{book["Title"]} is already on library!")

                line()
        
        else:

            line()

            print("Invalid ID!")

            line()
