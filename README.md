This project is an implementation of the Library Management System using OOP.

project is organize by the following file structure:
├── README.md                          # This file
│
├── procedural_version/
│   ├── library_procedural.py         # Original procedural code
│   └── test_procedural.py            # Comprehensive test suite
│
├── oop_solution/
│   ├── library_oop.py                # OOP implementation 
│   └── test_oop.py                   # Tests for OOP version

class Book:
attributes 
- id: id of the book
- title: Title of the book 
- author:	Author of the book
- total_copies: total copies of the book
- available_copies:	available copies of the book (initialy total copies)
key methods
- borrow_copy: check if available_copies if have the copies and subtract 1
- return_copy: check if available_copies is less than total_copies and add 1

class Member:
attributes 
- member_id: id of the member
- name: Name of the member
- email:	Email of the member
- borrowed_books: list of book ids
key methods
- borrowed_count: count the borrowed books in borrowed_books list
- borrow_book: check if the member have not reached the borrow limit
- return_book: check if the member have the book and remove it from borrowed_books list if they have it

class Library:
attributes 
- books: dictionary of books {id: Book}
- members: dictionary of members {id: Member}
key methods
- add_book: add book to the books dictionary
- add_member: add member to the members dictionary
- _find_book: check if the book exist
- _find_member: check if the member exist
- borrow_book: find the book and member, check for errors, call borrow_book from Member class
- return_book: find the book and member, check for errors, call return_book from Member class
- display_available_books: check if there's any books in books list and print out the book attributes if they have it
- display_member_books: check if there's any members in members list and print out the books each member has

Testing
I used the given tests from test_procedural.py and edit the code to fit with OOP to see if it works
