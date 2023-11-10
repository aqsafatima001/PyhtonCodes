# Q-:You have to create a library management System . This must be done by creating a class called library

# The class library should have the following functions:
# 1)display book: It displays all the books in the library along with wether they are available or lent to someone
# 2)lend book: This will allow the user to issue a book from the library. If the requested book is lent to someone
#              then print their name
# 3)add book: This fn is used to enter the name of the book to be added to the lib
# 4)return book : Allows the user to return a book

# The Constructor of the class should take 2 arguments:
# 1) a list of all the book in the lib
# 2) the name of the lib

# E.g:
# HarryLibrary = Library(listofbooks, library_name)

# You are to keep record of which book is issued to who via a dict as follows:
# key - name of the book
# value - name of the person issued to
# dictionary (books-nameofperson)

# create a main function and run an infinite while loop asking
# users for their input"""

#  ------------------------------------------------Library class starts here-----------------------------------------
import colorama
from colorama import Fore,Style,Back
class library:
    #Constructor
    def __init__(self,books,name):
        self.books = books
        self.name  = name
        self.dict  = {}
    
    # Function to display books
    def display_book(self):                                     
        print("The available books are:")
        for i in self.books:
            print(i, end=", ")
        print()
    
    #Lend Books function
    def lend_book(self):
        person = input("Please Enter your name: ")
        want = input("Enter the book you want to lend:")
        if want in self.books:
            print("Ok, You can take it!")
            self.dict[want] = person
            self.books.remove(want)
        elif want in self.dict :
            taker = self.dict[want]
            print(f"Sorry!it is already taken by {taker}")

        else:
            print("sorry! we don't have such a book")

    #Add boooks to the collection
    def add_book(self):
        new=input("Hey Admin! Enter the book which you want to add: ")
        print(Style.RESET_ALL)
        if new in self.books:
            print("This book is already present! please add another book...")
        elif new in self.dict:
            print("This book is already present in our library and taken by someone")
        else:
            print("Adding....")
            self.books.append(new)
            print("Successfully added!")

    #Return the book
    def return_book(self):
        ret=input("Enter the book name: ")
        if ret in self.dict:
            self.dict.pop(ret)
            self.books.append(ret)
            print("Successfully returned")
        elif ret in self.books:
            print("You have not issued it!")
        else:
            print("We dont have such books!")

    #Searching Book
    def search_book(self):
        find = input("Enter book name to check whether it is available or not: ")
        print("Searching...")
        if find in self.books:
            print("oh! great, this book is available in our library.")
        elif find in self.dict:
            print("This book is available in our library but currently issued by someone plz wait until its available for you...")
        else:
            print("sorry we don't have such books!")

name  = "\n*** Welcome to Aqsa's Library ***"

l1 = library(["pyhton" , "Java" , "C" , "C++", "NodeJS" , "WebDev", "JavaScript"],name)
print(l1.name)

while True:
    inp=(input(Fore.GREEN +"\nEnter 1 to display books: \nEnter 2 to lend a book: \nEnter 3 to add a new book: \nEnter 4 to return a book: \nEnter 5 to search a book: \nEnter 6 to exit:"))
    print(Style.RESET)
    if inp == '1' or inp == 'D' or inp == 'd':
        l1.display_book()
    elif inp == '2' or inp == 'L'  or inp == 'l':
        l1.lend_book()
    elif inp == '3' or inp == 'A' or inp == 'a':
        l1.add_book()
    elif inp == '4' or inp == 'R' or inp == 'r':
        l1.return_book()
    elif inp == '5' or inp == 'S' or inp == 's':
        l1.search_book()
    elif inp == '6' or inp == 'E' or inp == 'e':
        print("\t\t * Thanks for Using our facility! ***")
        break
    else:
        print("Invalid input!")
