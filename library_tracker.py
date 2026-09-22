# Library Tracker
# python essential project

File_Name = "Library.txt"

def load_books():
    books = []
    try:
        file = open(File_Name, "r")
        for line in file:
            data = line.strip().split("|")
            if len(data) == 5:
                # Dynamically set status based on the "issued_to" field
                status = "Issued" if data[4] else "Available"
                book = {
                    "id": data[0], 
                    "title": data[1], 
                    "author": data[2], 
                    "year": data[3], 
                    "status": status,
                    "issued_to": data[4]
                }
                books.append(book)
        file.close()
    except FileNotFoundError:
        print("Library file not found. Starting with an empty library.")

    return books

def save_books(books):
    # Corrected from tuple to open()
    file = open(File_Name, "w")
    for book in books:
        line = f"{book['id']}|{book['title']}|{book['author']}|{book['year']}|{book['issued_to']}\n"
        file.write(line)
    file.close()

def display_menu():
    print("\n=========")
    print("Library Tracker")
    print("=========")
    print("1. Add Book")
    print("2. View Books")  
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. View Issued Books")
    print("8. Exit")
    print("=========")

def add_book(books):
    print("\n-----ADD BOOKS------")
    book_id = input("Enter Book ID: ")
    
    # Check if book ID already exists   
    for book in books:
        if book["id"] == book_id:
            print("Book ID already exists. Please use a different ID.")
            return
            
    # Moved outside of the loop checking for duplicates
    title = input("Enter Book Title: ")
    author = input("Enter Book Author: ")
    year = input("Enter Book Year: ") # Added missing year input
    
    book = {
        "id": book_id, 
        "title": title, 
        "author": author, 
        "year": year, 
        "status": "Available", 
        "issued_to": ""
    }
    books.append(book)
    save_books(books) # Added missing save call
    print("Book added successfully.")

# Un-indented all subsequent functions so they are properly defined at the module level

def view_books(books):
    print("\n-----VIEW BOOKS------")
    if len(books) == 0:
        print("No books found.")
        return
    print("-" * 75)
    print("   ID Title  Author  Year  Issued To")
    print("-" * 75)   
    for book in books:
        print(f"{book['id']} {book['title']} {book['author']} {book['year']} {book['issued_to']}")
    print("-" * 75)

def search_book(books):
    print("\n-----SEARCH BOOKS------")
    search = input("Enter Book Title or Author to search: ").lower()
    found = False

    for book in books:
        if search in book["title"].lower() or search in book["author"].lower():
            print("\nBook Found:")
            print("Book ID:", book["id"])
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Year:", book["year"])
            print("Issued To:", book["issued_to"])
            found = True
            
    if not found:
        print("Book not found.")

def issue_book(books):
    print("\n-----ISSUE BOOKS------")
    book_id = input("Enter Book ID to issue: ")
    for book in books:
        if book["id"] == book_id:
            if book["status"] == "Issued":
                print("Book is already issued to", book["issued_to"])
                return
            student_name = input("Enter Student Name: ")
            book["status"] = "Issued" 
            book["issued_to"] = student_name
            save_books(books)
            print("Book issued successfully!")
            return
            
    # Moved outside the loop
    print("Book ID not found.")

def return_book(books):
    print("\n-----RETURN BOOKS------")
    book_id = input("Enter Book ID to return: ")
    for book in books:
        if book["id"] == book_id:
            if book["status"] == "Available":
                print("Book is not issued.")
                return
            book["status"] = "Available"
            book["issued_to"] = ""
            save_books(books)
            print("Book returned successfully!")
            return

    # Moved outside the loop
    print("Book ID not found.")

def delete_book(books):
    print("\n-----DELETE BOOKS------")
    book_id = input("Enter Book ID to delete: ")
    for book in books:
        if book["id"] == book_id:
            if book["status"] == "Issued":
                print("Book is currently issued and cannot be deleted.")
                return
            books.remove(book)
            save_books(books)
            print("Book deleted successfully!")
            return
            
    # Moved outside the loop
    print("Book ID not found.")

def view_issued_books(books):
    print("\n-----VIEW ISSUED BOOKS------")
    found = False
    for book in books:
        if book["status"] == "Issued":
            print("\nBook ID:", book["id"])
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Year:", book["year"])
            print("Issued To:", book["issued_to"])
            found = True

    if not found:
        print("No issued books found.")

def main():
    books = load_books()
    print("\n=======")
    print("  Welcome to Library Tracker")
    print("=======")

    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            add_book(books)
        elif choice == "2":
            view_books(books)
        elif choice == "3":
            search_book(books)
        elif choice == "4":
            issue_book(books)
        elif choice == "5":
            return_book(books)
        elif choice == "6":
            delete_book(books)
        elif choice == "7":
            view_issued_books(books)
        elif choice == "8":
            print("Exiting Library Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()