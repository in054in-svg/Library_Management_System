def show_menu() -> str:
    choice = input("""================================
       LIBRARY MANAGEMENT
================================

1. Display all books
2. Search book by name
3. Add new book
4. Borrow a book
5. Return a book
6. Display available books
7. Display books by author
8. Exit

Choose an option:
""" )
    return choice