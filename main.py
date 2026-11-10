import time
from output import show_menu
from books_management import display_books, search_book_management, add_book_management, borrow_and_return_book_management, get_available_books, search_book_by_author


books = [{"id": 1, "name": "Harry Potter", "author": "J.K. Rowling", "year": 1997, "available": True},    
         {"id": 2, "name": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937, "available": True},
         {"id": 3, "name": "Clean Code", "author": "Robert Martin", "year": 2008, "available": False},
         {"id": 4, "name": "Atomic Habits","author": "James Clear", "year": 2018, "available": True},
         {"id": 5, "name": "The Pragmatic Programmer", "author": "David Thomas", "year": 1999, "available": False}
         ]


if __name__ == '__main__':
    while True:
        choice = show_menu()
        match choice:
            case '1':
                display_books(books)
            case '2':
                print(search_book_management(books, 1))
            case '3':
                if add_book_management(books):
                    print('The book was added successfully!')
                else:
                    print('The book already exists!')
            case '4':
                if borrow_and_return_book_management(books, False):
                    print('The book was successfully borrowed!')
                else:
                    print('The book was not found')
            case '5':
                if borrow_and_return_book_management(books, True):
                    print('The book was successfully returned!')
                else:
                    print('The book was not found')
            case '6':
                available_books = get_available_books(books)
                if available_books:
                    print('\n'.join(map(str, available_books)))
                else:
                    print('There is no available books!')
            case '7':
                print(search_book_management(books, 0))
            case '8':
                break
            case _:
                print('Choose number between 1-8 only!')
                
        time.sleep(2)