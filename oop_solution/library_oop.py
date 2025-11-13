#I made all 3 class and tested them first before doing the seperate commit
#I save the texts in my notes then delete all the text in the file

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
        

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book: Book):
        self.books[book.id] = book
        print(f"Book '{book.title}' added successfully!")

    def add_member(self, member: Member):
        self.members[member.id] = member
        print(f"Member '{member.name}' registered successfully!")

    def _find_book(self, book_id):
        return self.books.get(book_id)

    def _find_member(self, member_id):
        return self.members.get(member_id)

    def borrow_book(self, member_id, book_id):
        member = self._find_member(member_id)
        book = self._find_book(book_id)

        if not member and not book:
            print("Error: Member or book not found!")
            return False   
        elif not member:
            print("Error: Member not found!")
            return False
        elif not book:
            print("Error: Book not found!")
            return False
        
        if member.borrowed_count() >= member.BORROW_LIMIT:
            print("Error: Member has reached borrowing limit!")
            return False

        if not book.borrow_copy():
            print(f"Error: No copies available!")
            return False

        member.borrow_book(book_id) 
        
        print(f"{member.name} borrowed '{book.title}'")
        return True

    def return_book(self, member_id, book_id):
        member = self._find_member(member_id)
        book = self._find_book(book_id)

        if not member and not book:
            print("Error: Member or book not found!")
            return False
        
        elif not member:
            print("Error: Member not found!")
            return False
        
        elif not book:
            print("Error: Book not found!")
            return False

        if not member.return_book(book_id):
            print("Error: This member hasn't borrowed this book!")
            return False

        book.return_copy()
        
        print(f"{member.name} returned '{book.title}'")
        return True

    def display_available_books(self):
        print("\n=== Available Books ===")
        found = False
        for book in self.books.values():
            if book.available_copies > 0:
                print(f"{book.title} by {book.author} - {book.available_copies} copies available")
                found = True
        if not found:
            print("No books currently available.")

    def display_member_books(self, member_id):
        member = self._find_member(member_id)
        if not member:
            print("Error: Member not found!")
            return
        
        print(f"\n=== Books borrowed by {member.name} ===")
        if not member.borrowed_books:
            print("No books currently borrowed")
            return

        for book_id in member.borrowed_books:
            book = self._find_book(book_id)
            if book:
                print(f"- {book.title} by {book.author}")