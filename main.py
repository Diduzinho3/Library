from defs import (
    create_new_book,
    show_book_list,
    search_title,
    remove_by_id,
    borrow_book,
    return_book,
    save_books,
    line
)

program = True

while program:

    choose = input("""1 - Create New Book
2 - Book List
3 - Title Search
4 - Remove by ID
5 - Borrow Book
6 - Return Book
L - Finish Program

Choose: """).upper()

    if choose == "1":

        create_new_book()

    elif choose == "2":

        show_book_list()

    elif choose == "3":

        search_title()

    elif choose == "4":
        
        user_id = int(input("Book ID: "))
        remove_by_id(user_id)
    
    elif choose == "5":

        user_id = int(input("Book ID: "))
        borrow_book(user_id)

    elif choose == "6":

        user_id = int(input("Book ID: "))
        return_book(user_id)

    elif choose in ["L", "LE", "LEA", "LEAV", "LEAVE"]:

        line()

        program = False

        print("Finishing program!")

        line()

    else:

        line()

        print("Error! Choose one of the choices!")

        line()
