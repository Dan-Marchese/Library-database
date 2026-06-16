import datetime
        #Importing a date time function for library rental functions

class Book:
        #Create a class for book that represents a single book in the library,
        #Allows functions to be added to the class for further use.

    def __init__(self, book_id, title, author):
        self.id = book_id
        self.title = title
        self.author = author
        self.borrower = None
        self.borrow_date = None
        self.status = "available"
        #Create attributes for book ID, title and author using the arguments included.
        #Builds attributes for borrower and borrow_date as well as status being set to 'available' initially.

    def borrow(self, borrower_name):
        self.borrower = borrower_name
        self.borrow_date = datetime.date.today().isoformat()
        self.status = "borrowed"
        #Define a method 'borrow' to update the books status when borrowed, allowing for the following;
        #Name of borrower, record today's date as borrow date in ISO format (YYYY-MM-DD),
        #Change books status to 'borrow' from 'available'.

    def return_book(self):
        self.borrower = None
        self.borrow_date = None
        self.status = "available"
        #Define a method to return a book, removes borrower name and borrow date,
        #And set the status back to 'available'.

    def is_borrowed(self):
        return self.status == "borrowed"
        #Define a method to check whether a book is already borrowed.

    def matches_query(self, query):
        query = query.lower()
        return query in self.title.lower() or query in self.author.lower()
        #Define method to search for a book or author that is not case-sensitive.
        #For example if searching for an author Smith, you can enter SMITH, Smith, or smith,
        #And still return the same matches.

    def display(self):
        print(f"id: {self.id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {self.status}")
        if self.is_borrowed():
            print(f"Borrower: {self.borrower}")
            print(f"Borrow Date: {self.borrow_date}")
        print("-" * 20)
        #Define a method for display and print the details of a book.
        #Create an if statement if the book is borrowed to print who has borrowed the book and the date borrowed.
        #Prints a line of 20 times '-' to visually separate display searches.

class Library:
        #Create a class 'library'

    def __init__(self):
        self.catalogue = []
        #Defines method that runs when you create a library object, and stores objects into an empty catalogue.

    def add_book(self, book_id, title, author):
        if self.find_book(book_id):
            return False
        self.catalogue.append(Book(book_id, title, author))
        return True
        #Method to add a book to the library class using ID, title and author.
        #If statement to check if a book with the created name already exists, preventing duplicate books being created.
        #Creates the book with the details given, and adds them to the catalogue and returns True when successful.

    def find_book(self, book_id):
        for book in self.catalogue:
            if book.id == book_id:
                return book
        return None
        #Method to find a book by the book ID inside the library, if book is found it will return the match.
        #If no matching book is found it will return none.

    def borrow_book(self, book_id, borrower):
        book = self.find_book(book_id)
        if not book or book.is_borrowed():
            return None
        book.borrow(borrower)
        return book
        #Method to borrow book from library using the find book method previously created.
        #Checks if the book is recognised or already borrowed before allowing a new instance to borrow the book.


    def return_book(self, book_id):
        book = self.find_book(book_id)
        if not book or not book.is_borrowed():
            return None
        book.return_book()
        return book
        #Method to return a book, uses the find book method previously created.
        #Checks if book is recognised or not borrowed before allowing the book to be returned.

    def search(self, query):
        return [b for b in self.catalogue if b.matches_query(query)]
        #Method to return a list of books from the catalogue that match a given query.

    def get_borrowed_books(self):
        return [b for b in self.catalogue if b.is_borrowed()]
        #Method to filter search by books that are already borrowed.

    def count_borrowed_books(self):
            return len(self.get_borrowed_books())
        #Method to count the amount of books currently borrowed and return in a how many appear.

    def display_all(self):
        if not self.catalogue:
            print("No books in the catalogue.")
            return
        for book in self.catalogue:
            book.display()
        #Method to print and display all books in catalogue.
        #If no books in catalogue print 'no books...'

    def display_borrowed(self):
        borrowed = self.get_borrowed_books()
        if not borrowed:
            print("No books are currently borrowed out.")
            return
        for book in borrowed:
            book.display()
        #Method to print all books currently borrowed,
        #If no books borrowed print 'no books...'

def print_menu():
    print("\nCommunity Library")
    print("[1] Add Book")
    print("[2] Borrow Book")
    print("[3] Return Book")
    print("[4] View Catalogue")
    print("[5] View Borrowed Books")
    print("[6] Search Books")
    print("[7] Count Borrowed Books")
    print("[8] Exit")
        #Method for the user interface and options available for the user.

def main():
    library = Library()
        #Creates a library object and instance of library

    while True:
        print_menu()
        choice = input("Select an option: ").strip()
        #Creates an infinite loop waiting for a user choice.

        if choice == "1":
            print("\n--- Add Book ---")
            book_id = input("Book ID: ").strip()
            title = input("Title: ").strip()
            author = input("Author: ").strip()
            if library.add_book(book_id, title, author):
                print("Book added successfully.")
            else:
                print("A book with that ID already exists.")
        #Creates a loop for option 1, attempts to add the book, and prints when successful or not.

        elif choice == "2":
            print("\n--- Borrow Book ---")
            book_id = input("Book ID: ").strip()
            borrower = input("Borrower Name: ").strip()
            book = library.borrow_book(book_id, borrower)
            if book:
                print(f"Book '{book.title}' Borrowed to {borrower}.")
            else:
                print("Book not found or already Borrowed.")
            #Loop that works only when option 2 is selected. Allows user to borrow a book when they input their
            #Details and returns when borrowed
            #Returns when book is not found or already borrowed.

        elif choice == "3":
            print("\n--- Return Book ---")
            book_id = input("Book ID: ").strip()
            book = library.return_book(book_id)
            if book:
                print(f"Book '{book.title}' returned.")
            else:
                print("Book not found or not currently borrowed.")
            #Loop for option 3 that allows user to return a book
            #Returns if book is not borrowed or not found

        elif choice == "4":
            print("\n--- Catalogue ---")
            library.display_all()
            #Prints 'Catalogue' and displays all books.

        elif choice == "5":
            print("\n--- Borrowed Books ---")
            library.display_borrowed()
            #Displays all currently borrowed books

        elif choice == "6":
            print("\n--- Search ---")
            query = input("Enter title or author: ").strip()
            results = library.search(query)
            if results:
                for b in results:
                    b.display()
            else:
                print("No matching books found.")
            #Allows user to search for a book by title or author and displays the results.
            #If no result matches prints 'no matching books found'

        elif choice == "7":
            print(f"\nBooks currently borrowed out: {library.count_borrowed_books()}")
            #Display books currently borrowed

        elif choice == "8":
            print("Goodbye.")
            break
            #Creates an option for the user to exit the loop and prints 'Goodbye' to the user.

        else:
            print("Invalid option. Try again.")
            #Prints only when an invalid option is made during the user input process and allows them to try again.

if __name__ == "__main__":
    main()
            #Ensures file is run directly when the file is the main program and starts the main program including
            #The library object