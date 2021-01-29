# Software Requirement Specification (SRS) document for Library-Management-System
## 1.	Introduction
Even in this time of modern technology, many libraries depends on the manual working for management of user records and book transactions. 
To overcome this, we introduce a Graphical User Interface (GUI) application by the name ‘Library Management System’ where all the
information of a particular library is stored on a central database which can be accessed only with proper authorisation.
The stored information includes user details, book details, available books, book issue and return dates, and fine
(In case a user fail to return the book within the given time period). This is a user friendly application that helps in
better book circulation and monitor transactions.

### 1.1	Purpose  
The key purpose of this project is to eliminate the paper work required to maintain records of user details and the book transactions. 
This application makes it easy for all the users to search for the available books along with their precise location inside the 
library. It makes the process of issuing and returning a book easy and quick.

### 1.2	Document Conventions
- Admin	- The librarian
- User	- Person borrowing a book
- DB	- Database
- Sqlite3	- Relational database
- LMS	- Library Management System


### 1.3	Intended Audience and Reading Suggestions
The intended audience for this document are library staff, students, developers and documentation writers. The further explanation
is based on the overall description, functional and non-functional requirements, user stories and test plan of the project. 
The ‘Table of contents’ at the beginning can be referred to navigate to the desired part of this document.

### 1.4	Product Scope
The ‘Library Management System’ is a GUI application that is developed using Python programming language. It has complete information of the library in a central database. It consists of the following features.
-	Safety – Both the Admin and the users have to login with proper authorization (username and password).
-	The users has to first register on the application before borrowing a book.
-	The users can check their records and available books along with their location.
-	The admin can add, remove, issue and return the book.
-	Reminding the user about the return date.
-	Calculates fine for late submission of books.

### 1.5	References
* [Python tkinter](https://docs.python.org/3/library/tkinter.html)
* [Python Sqlite3](https://docs.python.org/3/library/sqlite3.html)
#### Other references:
- [educative.io](https://www.educative.io/courses/grokking-the-object-oriented-design-interview/RMlM3NgjAyR)
- [wordpress preplibs](https://preplibs.wordpress.com/library-management-systems/)



## 2.	Overall Description
### 2.1	Software Architecture
This Library Management System (LMS) Software is a new system designed to bring about more effective and efficient monitoring and controlling of the transactions in the library so that it gives a complete information about the library at any point in time.

### Context Diagram

The Context Diagram defines the interfaces between the internal and external systems. It is made up of the internal system – the Library Management System interacting with the external systems – the Actors, which include the Users, Administrators, Book and Catalogue. The Users interact with the Library Management System physically using the Screen and Keyboard and logically, using the GUI. Similarly, the Administrators interact with the Library Management System physically using the Screen and Keyboard and logically, using the GUI. Additionally, The Book interact with the Library Management System physically using the laser beam, and logically, using the barcode.

![context diagram](https://user-images.githubusercontent.com/45924101/105904998-d17cd480-6019-11eb-944e-31639c1543b4.PNG)
### Figure 1: The Context Diagram showing the interfaces between the internal and external systems in the Library Management System Software.


 ### Class Diagram 

The class diagram shows the classes in the system and their associations. The classes include Library, Book, Library Member, Users and Administrators classes. The Library class is composed of the Book class and a library can have one or more books. Furthermore, the Library Member class is a part of the Library class and a library can have one or more Library member. Additionally, The Library Member class generalizes the Users and Administrator classes.

![class diagram](https://user-images.githubusercontent.com/45924101/106309367-e778d800-6259-11eb-857e-9a364373431f.PNG)
### Figure 2: The class diagram showing the classes in the Library Management System and their interactions.


### 2.2	Product Functions and Use Cases
The Library Management System Software will allow the following users to perform the functions below as also represented in the use case diagram showing what the system.

Users will be able to do the following:
-	Register
-	Login
-	Check available books
-	Check their records
-	Check fine
-	Logout

Administrator – The library staffs will be able to do the following:
-	Login
-	Add/update members
-	Add/update books 
-	Issue books to the members 
-	Maintain member’s records 
-	Check available books
-	Check user records
-	Manage return
-	Send reminders
-	Issue fine

![use case diagram](https://user-images.githubusercontent.com/45924101/106310562-a5e92c80-625b-11eb-81b7-01cf8b5b73d4.PNG)
Figure 3: A use case diagram illustrating the work of Library Management System.

### 2.3	User and Stakeholders
The stakeholders of the LMS software are categorized as 

Users which could be:
-	Students
-	Teachers
-	Professors 
-	Workers 
-	Library workers 

Administrators – The library staffs could be:
-	Library Management System application administrator
-	IT administrator - Manages all applications in the Library
-	Security manager - Responsible for security issues
-	DB administrator - Manages DBMSs on which applications are based
-	Buyer - CEO and/or CTO or CIO of library

### 2.4	Operating Environment
#### 2.4.1 Software Requirement
-	Python IDE
-	Windows 7 or higher
-	Sqlite3

#### 2.4.2 Hardware Requirement
-	Minimum Intel i3
-	4GB Ram or higher
-	1.2 GHz processor or higher

