import psycopg2 as pg
import pandas as pd
import pandas.io.sql as psql
import warnings

try:
    connect = pg.connect(database = 'librarydb', user='postgres', password='moiz', host='localhost', port= '5432')
    connect.autocommit = True
    cursor = connect.cursor()
except:
    print("Can't Connect now! Try again later \nApologies...")

warnings.filterwarnings('ignore')

def insertBook():
    id = int(input("Enter Book Id: "))
    book = input("Enter Book's Name: ")
    
    sql = f"SELECT CASE WHEN EXISTS (SELECT * FROM books WHERE book_id= {id}) THEN 1 ELSE 0 END"
    check = cursor.execute(sql)
    
    # print(check)
    if check: print("Book already exist!")
    else:
        publishdate = input("Enter Publish Date (in format dd.mm.yyyy) : ")
        author = input("Enter Author's name: ")
        sql = f"INSERT INTO books(book_id, book_name, publish_date, author_name) VALUES ({id},'{book}','{publishdate}','{author}')"
        cursor.execute(sql)        
        print(f"{book} added successfully!")
        


def showLibrary():
    check = f"SELECT CASE WHEN EXISTS (SELECT * FROM books LIMIT 1) THEN 1 ELSE 0 END"
    if(check):
        sql = f"SELECT * FROM books ORDER BY book_id ASC"
        table = pd.read_sql(sql, connect)
        print(table)

    else:
        print("Library is Empty!")

def searchBook():
    book = input("Enter Book's Name: ")
    check = f"SELECT CASE WHEN EXISTS(SELECT * FROM books WHERE book_name='{book}') THEN 1 ELSE 0 END;"
    if(check):
        sql = f"SELECT book_name, author_name FROM books WHERE book_name='{book}';"
        table = pd.read_sql(sql, connect)
        print(table)
    else:
        print("Book doesn't exist")

def deleteBook():
    book = input("Enter Book to Delete: ")
    check = f"SELECT CASE WHEN EXISTS(SELECT * FROM books WHERE book_name='{book}') THEN 1 ELSE 0 END;"
    if(check):
        sql = f"DELETE FROM books WHERE book_name='{book}';"
        cursor.execute(sql)
        print(f"{book} deleted Successfully!" )

def getAuthor():
    book = input("Enter Book Name: ")
    check = f"SELECT CASE WHEN EXISTS(SELECT * FROM books WHERE book_name='{book}') THEN 1 ELSE 0 END;"
    if(check):
        sql = f"SELECT author_name FROM books WHERE book_name='{book}';"
        table = pd.read_sql(sql, connect)
        print(table)
        
