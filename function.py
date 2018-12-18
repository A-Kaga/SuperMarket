import pymysql


'''
This file contains some function:
connect_database()----connect with the database supermarket
'''

def connect_database():
    # my_id = input('User Account: ')
    # my_password = input('Password: ')
    return pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='ctj20100030928',
                           database='supermarket')