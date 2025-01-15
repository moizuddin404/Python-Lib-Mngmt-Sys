import libfunctions as lf
import psycopg2 as pg # type: ignore
import pandas as pd
import pandas.io.sql as psql

try:
    connect = pg.connect(database = 'librarydb', user='postgres', password='moiz', host='localhost', port= '5432')
    connect.autocommit = True
    cursor = connect.cursor()
except:
    print("Can't Connect now! Try again later \nApologies...")



print("\n\nWelcome to Moiz Library!")
print("------------------------")

choice = 1

while(choice!=0):
    print("\n1. View Library \n2. Insert a Book \n3. Search a Book \n4. Delete a Book \n5. Get Author's Name \n0 - Quit")
    choice = int(input("Your Choice: "))
    
    if choice == 1:
        lf.showLibrary()
    elif choice == 2:
        lf.insertBook()
    elif choice == 3:
        lf.searchBook()
    elif choice == 4:
        lf.deleteBook()
    elif choice == 5:
        lf.getAuthor()
    elif choice == 0:
        print("Thank you! See ya later.")
        break
