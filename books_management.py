from validation import get_positive_num, get_valid_str

def display_books(books: list) -> None:
    for book in books:
        print(book)
        
def search_book_management(books:list, search_type: int) -> list|None:

    name = get_valid_str('Enter a name:')
    if search_type:
        result = search_book(books, name)
    else:
        result = search_book_by_author(books, name)
    return result if result else "The book was not found"
        
def search_book(books:list , name:str) -> list|None:
    result = list(filter(lambda b: b['name'] == name, books))
    return result if result else None

def search_book_by_author(books:list ,author: str) -> list|None:
    result = list(filter(lambda b: b['author'].replace('. ', '.') == author.replace('. ', '.'), books))
    return result if result else None


def search_book_by_id(books:list , book_id: int) -> bool|int:
    result = list(filter(lambda b: b['id'] == book_id, books))
    return False if not result else books.index(result[0])

def get_next_book_id(books: list) -> int:
    return len(books) + 1
   
def add_book_management(books: list) -> bool:
    name = get_valid_str('Enter a book name:')
    author = get_valid_str("Enter an author's name:")
    year = get_positive_num('Enter publication year:')
    
    if search_book(books, name) and search_book_by_author(books, author):
        return False
    return add_book(books, name, author, year)    
    
def add_book(books:list , name: str, author: str, year: int) -> True:
    new_id = get_next_book_id(books)
    books.append({"id": new_id, "name": name, "author": author, "year": year, "available": True})
    return True

def borrow_and_return_book_management(books: list, action: bool) -> bool:
    book_id = get_positive_num('Enter book id:')
    return borrow_and_return_book(books, book_id, action)   
    
def borrow_and_return_book(books: list, book_id: int, action: bool) -> bool:
    the_index_in_books = search_book_by_id(books, book_id)
    if the_index_in_books is False:
        return False
    
    books[the_index_in_books]['available'] = action
    return True

def get_available_books(books: list) -> list:
    return list(filter(lambda b: b['available'], books))