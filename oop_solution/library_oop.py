class Book:
    def __init__(self, id, title, author, total_copies):
        self.id = id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies
        
    def borrow_copy(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        return False
    
    def return_copy(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1


class Member:
    BORROW_LIMIT = 3

    def __init__(self, member_id, name, email):
        self.id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []

    def borrowed_count(self):
        return len(self.borrowed_books)

    def borrow_book(self, book_id):
        if self.borrowed_count() < self.BORROW_LIMIT:
            self.borrowed_books.append(book_id)
            return True
        return False

    def return_book(self, book_id):
        try:
            self.borrowed_books.remove(book_id)
            return True
        except ValueError:
            return False