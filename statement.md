# Library Tracker — Project Statement

## 1. Problem Statement

Managing library books manually can become difficult as the number of books increases. It can be challenging to keep track of book details, available books, issued books, returned books, and deleted records using manual methods.

The **Library Tracker** project aims to provide a simple command-line application that helps users manage basic library book records efficiently. The system allows users to add, view, search, issue, return, and delete books while storing the records in a text file for future use.

---

## 2. Scope of the Project

The scope of the Library Tracker project is to provide basic book management functionality for a small library or educational environment.

The project includes:

* Adding new books with a unique Book ID
* Viewing all available book records
* Searching for books by title or author
* Issuing available books to students
* Returning issued books
* Deleting available books
* Viewing currently issued books
* Storing book information in `books.txt`
* Loading previously saved records when the program starts
* Handling basic invalid operations such as duplicate Book IDs and issuing an already issued book

The current project is designed as a command-line application and does not include advanced features such as database management, user authentication, online access, or a graphical interface.

---

## 3. Target Users

The primary target users of the Library Tracker are:

### Librarians

Librarians can use the application to maintain book records and manage basic issue and return operations.

### Students

Students can benefit from the system by allowing library staff to quickly search for books and check their availability.

### Small Educational Libraries

The application can be used as a simple record-management system for small schools, colleges, classrooms, or personal book collections.

### Python Learners

The project can also be used as an educational example for students learning fundamental Python programming concepts.

---

## 4. High-Level Features

The main features of Library Tracker are:

1. **Add Book**
   Allows the user to add a new book with a unique Book ID, title, and author.

2. **View All Books**
   Displays all books stored in the library records along with their current status.

3. **Search Book**
   Allows users to search for a book using its title or author.

4. **Issue Book**
   Allows an available book to be issued to a student.

5. **Return Book**
   Allows an issued book to be returned and marked as available.

6. **Delete Book**
   Allows an available book to be removed from the records.

7. **View Issued Books**
   Displays all books that are currently issued and the students who have them.

8. **Persistent Storage**
   Stores book records in `books.txt` so that the data can be loaded again when the program is restarted.

9. **Basic Validation**
   Prevents duplicate Book IDs and invalid operations such as issuing an already issued book or deleting an issued book.
