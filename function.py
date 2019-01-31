import pymysql


def connect_database():
    # my_id = input('User Account: ')
    # my_password = input('Password: ')
    return pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='ctj20100030928',
                           database='supermarket')

'''
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


def stock_update(id, mode, amount):
    db = connect_database()
    cursor = db.cursor()
    search_sql = """
                 SELECT MIN_STOCK, MAX_STOCK
                 FROM WARE_DATA
                 WHERE WARE_ID = %s
                 """
    stock_sql = """
                SELECT AMOUNT
                FROM STOCK_DATA
                WHERE WARE_ID = %s
                """
    update_sql = """
                 UPDATE STOCK_DATA
                 SET AMOUNT = %s
                 WHERE WARE_ID = %s 
                 """
    
    cursor.execute(search_sql, id)
    stock_range = cursor.fetchone()
    cursor.execute(stock_sql, id)
    stock = cursor.fetchone()
    modified_amount = int(mode) * int(amount) + int(stock[0])
    print(modified_amount)

    if modified_amount < stock_range[0]:
        print("少了")
    elif modified_amount > stock_range[1]:
        print("多了")
    else:
        sql_data = [modified_amount, id]
        cursor.execute(update_sql, sql_data)
        db.commit()
    '''
    这里错误处理不过关！！！
    '''