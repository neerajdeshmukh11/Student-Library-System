# Library Management System


class library:
    def __init__(self, listofbooks):
        self.books = listofbooks

    def displayAvailableBooks(self):
        print("welcome to our library!!!" + "\n the list of books are:")
        for books in self.books:
            print(" *" + books)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued  the book {bookName}")
            self.books.remove(bookName)
            return True
        else:
            print(f"sorry {bookName} is alread issued by someone!!")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print(f"Thanks for returning {bookName} book,, Have a good day ahead!!")


class Student:
    def requestBook(self):
        self.book = input("Enter the name of book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of book you want to return: ")
        return self.book


if __name__ == "__main__":
    CentralLibrary = library(["let's C", "Python", "Django", "C++", "Algorithms"])
    student = Student()
    # CentralLibrary.displayAvailableBooks()
    while True:
        welcomesg = """***Welcome to central library***
        choose an option
        1. Display the books
        2. Borrow a book
        3. Return a book
        4. Exit the library """
        print(welcomesg)
        a = int(input("Enter a choice: "))
        if a == 1:
            CentralLibrary.displayAvailableBooks()
        elif a == 2:
            CentralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            CentralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanku for visiting central library!!, Have a nice day ahead!!")
            exit()
        else:
            print("Invalid choice")    
