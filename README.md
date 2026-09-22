# LibraryTracker

# Library Tracker

## 1. Project Overview

**Library Tracker** is a simple command-line Library Management System developed using Python. It helps manage basic library operations such as adding books, viewing books, searching for books, issuing books, returning books, deleting books, and viewing currently issued books.

The project is designed as a Python Essential course project and uses fundamental Python concepts such as functions, lists, dictionaries, loops, conditional statements, string operations, exception handling, and file handling.

Book records are stored in a text file named `books.txt`, allowing the data to remain available after the program is closed.

---

## 2. Features

The project provides the following features:

* Add a new book
* View all books
* Search for a book by title or author
* Issue a book to a student
* Return an issued book
* Delete a book
* View currently issued books
* Prevent duplicate Book IDs
* Prevent issuing an already issued book
* Prevent returning an already available book
* Prevent deleting an issued book
* Save book records permanently in `books.txt`

---

## 3. Technologies / Tools Used

### Programming Language

* **Python 3**

### Python Concepts Used

* Variables
* Strings
* Lists
* Dictionaries
* Functions
* `if-elif-else` statements
* `for` loops
* File handling
* Exception handling
* String methods

### Tools

* Python 3.x
* Command Prompt / Terminal
* GitHub

### External Dependencies

No external Python libraries are required.

The project uses only Python's built-in features.

---

## 4. Project Structure

```text
LibraryTracker/
│
├── library_tracker.py
├── books.txt
└── README.md
```

### Files

**`library_tracker.py`**
Contains the complete Library Tracker program.

**`books.txt`**
Stores the book records used by the application.

**`README.md`**
Contains project documentation and instructions.

---

## 5. Installation & Setup

### Step 1: Install Python

Install Python 3.x on your computer.

Check whether Python is installed by opening Command Prompt or Terminal and running:

```bash
python --version
```

If your system uses `python3`, run:

```bash
python3 --version
```

---

##

Step 2: Clone the GitHub Repository

Clone the project using:

git clone https://github.com/utkarshtiwari22243659-jpg/LibraryTracker.git
Step 3: Open the Project Directory
cd LibraryTracker
Step 4: Check the Project Files

The directory should contain:

library_tracker.py
books.txt
README.md
Step 5: Install Dependencies

No external dependencies are required.

Therefore, no pip install command is necessary.

6. How to Run the Project

Run the following command:

python library_tracker.py

If your system uses python3, run:

python3 library_tracker.py

The program will start in the terminal and display the main menu.

Example:

====================================
      WELCOME TO LIBRARY TRACKER
====================================

====================================
          LIBRARY TRACKER
====================================
1. Add Book
2. View All Books
3. Search Book
4. Issue Book
5. Return Book
6. Delete Book
7. View Issued Books
8. Exit
====================================
Enter your choice:

Enter the number corresponding to the operation you want to perform.

7. Data Storage

The project uses books.txt for storing book information.

Each book is stored in the following format:

Book_ID|Title|Author|Status|Issued_To

Example:

B101|Python Basics|John Smith|Available|
B102|Data Structures|Robert Brown|Issued|Rahul

The | symbol separates the different fields.

The program automatically reads the saved records when it starts and updates the file whenever a book is added, issued, returned, or deleted.

8. Instructions for Testing

The following test cases can be used to verify the project.

Test 1: Add Book
Run the program.
Select option 1.
Enter a unique Book ID.
Enter the book title.
Enter the author name.

Expected result:

Book added successfully!
Test 2: View Books
Select option 2.

Expected result:

All stored books should be displayed with their ID, title, author, and status.

Test 3: Search Book
Select option 3.
Enter a book title or author name.

Expected result:

The matching book information should be displayed.

Test 4: Issue Book
Select option 4.
Enter the ID of an available book.
Enter the student's name.

Expected result:

Book issued successfully!

The status should change from:

Available

to:

Issued
Test 5: Return Book
Select option 5.
Enter the ID of an issued book.

Expected result:

Book returned successfully!

The status should change back to:

Available
Test 6: Delete Book
Select option 6.
Enter the ID of an available book.

Expected result:

Book deleted successfully!
Test 7: Duplicate Book ID

Try adding a book using an existing Book ID.

Expected result:

Book ID already exists.
Test 8: Issue an Already Issued Book

Try issuing a book whose status is already Issued.

Expected result:

Book is already issued.
Test 9: Persistence Test
Add one or more books.
Exit the program.
Start the program again.
Select View All Books.

Expected result:

Previously saved books should still be available.

Test 10: Invalid Menu Choice

Enter a number that is not between 1 and 8.

Expected result:

Invalid choice. Please try again.
9. Screenshots

Screenshots are optional but recommended.

The following screenshots can be added to demonstrate the working of the project:

Main menu
Adding a book
Viewing all books
Searching for a book
Issuing a book
Viewing issued books
Returning a book
Deleting a book
books.txt showing stored records

Example screenshot section:

### Main Menu

<img width="1920" height="1080" alt="Screenshot 2026-09-22 215312" src="https://github.com/user-attachments/assets/abdab0d8-e556-4e26-9fec-480a57e3b99a" />


### Adding a Book
<img width="1920" height="1080" alt="Screenshot 2026-09-22 220630" src="https://github.com/user-attachments/assets/e0976287-55da-41d7-8fb3-cdcb566124f4" />


### Issuing a Book

<img width="1920" height="1080" alt="Screenshot 2026-09-22 220650" src="https://github.com/user-attachments/assets/fc45d29a-7462-4c10-afaa-e5a029f2b643" />


### Returning a Book

[Insert screenshot here]

Use actual screenshots of your own program execution rather than fabricated images.

10. Expected Result

After successful execution, the application should allow the user to manage the complete basic lifecycle of a book:

Add → View → Search → Issue → Return → Delete

The book information should remain stored in books.txt between program executions.

11. Limitations
The application works through the command line.
It does not use a graphical interface.
It does not use a database.
It does not have user authentication.
It does not calculate fines or due dates.
It is intended for a small library dataset.
12. Future Enhancements

The project can be extended by adding:

Graphical User Interface (GUI)
Database integration
Student/member management
Login and authentication
Due dates
Fine calculation
Book categories
Multiple copies of books
Web-based interface
Library reports and statistics
13. Author

Name: Utkarsh Tiwari
Course: Python Essential / Introduction to Problem Solving and Programming
Academic Year: 2026–27

14. Conclusion

Library Tracker is a simple Python-based application that demonstrates how fundamental programming concepts can be used to solve a practical library management problem.

The project provides basic book management functionality, persistent file storage, and command-line execution without requiring external Python libraries.
