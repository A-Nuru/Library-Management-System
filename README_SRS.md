# Software Requirement Specification (SRS) document for Library-Management-System
## 1.	Introduction
Even in this time of modern technology, many libraries still manage user records and book transactions manually. 
To overcome this challenge, we introduce a Graphical User Interface (GUI) application by the name ‘Library Management System’ where all the
information of a particular library is stored on a central database which can be accessed only with proper authorisation.
The stored information include user details, book details, available books, book issue and return dates, and fine
(In case a user fail to return the book within the given time period). This is a user friendly application that aids
book circulation and transaction monitoringin a library.

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



### 2.5	Design and Implementation Constraints
-	The LMS software should be written in English because it is the language the users understand.
-	Easy to use system design so that the users of the software can adapt quickly to it.
-	The LMS software must be secured and safe enough so that the library services are not redirected.
-	Book update must be recorded to have updated & correct values.
-	Member update must be recorded to have updated & correct names.
-	Members should be notified of accurately calculated fines as soon as possible

### 2.6	User Documentation
A procedural guide will be associated with the Library Management software to guide new users, especially the administrators how to use the software. This will teach new users the best guideline practices and the most effective commands. This will include a user manual in text format and videos describing how to use the GUI.

### 2.7	Assumptions and Dependencies
The LMS software is dependent on the latest version of following libraries
-	Tkinter
-	Sqlite3
-	Pillow
-	Twilio

The LMS software is assumed to be used on a computer with enough performance ability, with an up-to-date internet browser. The LMS software might not work as intended if the computer does not have enough performance to support its backend, which may lead to performance and usability issues for the user. The user is also assumed to complete a training session by going through the manual and video associated with the software so as to be able to use it effectively and efficiently.


## 3.	External Interface Requirements
### 3.1	User Interfaces
Registration Interface: If a user is not registered to the application, they can register themselves by using the sign up function. In which they have to submit university Id, choose password and mobile number.

Login Interface: The users can sign in to their respective accounts with correct username and password. In case, if the password is incorrect they will not be able to log in.

Admin Interface: In this interface, the administrator can add, issue, return and manage books. The admin can also remind the user about their book return dates.

Search Interface: The user can search for the books by the book name/author/genre. If the searched item is available in records then it will get displayed. Linear search function is used for searching operation.


### 3.2	Hardware Interfaces
The minimum hardware requirement for this project are described below.

-	Processor: Intel core i3
-	Ram: 4 Gigabytes
-	Storage: 10 Gigabytes

### 3.3	Software Interfaces
This application is developed using Python programming language and Sqlite3 database is used to store its data.

-	Operating System: Windows 7 or higher/ MAC/ UNIX
-	Python Idle

### 3.4	Communications Interfaces
Twilio – It is a cloud communication platform, which allows software developers to programmatically send/receive SMS using its web APIs. To install Twilio library in Python application, we can use the pip method as follows.
- pip install twilio
To use twilio SMS communication in the program, we have to first signup on twilio.com and it will provide us the trial number and account details (Account Sid, Authorization Token). These details are used inside the code to send free SMS.

## 4.	System Requirements

### 4.1	Registration: F1
#### 4.1.1	Description and Priority
A person who wants to borrow a book from the library should register on the application by using the Sign up function. This is mandatory and has a very high priority because there must be record for each user of the LMS app and  the records will be stored in a central database. These user informations are highly important for users in order to have access to the library transactions, for instance, issuing a book.

#### 4.1.2    Input/Outputs Sequences
While signing up, the user have to add his UEL id as username, a strong password and his mobile number and then click on sign up button. If all the information is valid, then a message box pops up stating 'registration successful'. If the information is not valid or wrong or any entry fields are empty, then an error message pops out.

#### 4.1.3	Functional Requirements
- F1.1: Tkinter

This is a Python library that helps in creating GUI application and is needed to run this software. A user can install the Tkinter library by using pip command and import the library in the program by using the code below.

Installation: pip install Tkinter
Importing: Import Tkinter as tk

- F1.2: Sqlite3

Sqlite3 is a database management system, which allows the application to securely store the user information inside a database. User can use pip command to install the sqlite3 library and import function to use the library.

Installation: pip install sqlite
Importing: Import sqlite3

- F1.3: Tkinter Message Box

Message Box is a part of Tkinter library which is used to convey an error or success information in a small box. User has to import this separately from Tkinter by using the below command

Importing: from tkinter import messagebox
	

