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

def ware_check(id, amount, cursor):
    quantity_sql =
    """
    SELECT QUANTITY FROM WARE_DATA
    """
    min_sql =
    """
    SELECT MIN_STOCK FROM WARE_DATA
    """
    max_sql =
    """
    SELECT MAX_STOCK FROM WARE_DATA
    """
    cursor.execute(quantity_sql)
    quantity = cursor.fetchone()

    '''
    未完成：
    数据连接
    '''