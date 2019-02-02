import pymysql

'''
存在的问题：
sql语句能不能集中保存，直接调用，现目前复用性不高
尽可能提高各功能的复用性
'''

def connect_database():
    # my_id = input('User Account: ')
    # my_password = input('Password: ')
    return pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='ctj20100030928',
                           database='supermarket')


def ware_id_check(id):
    db = connect_database()
    cursor = db.cursor()
    search_sql = """
                 SELECT 1
                 FROM WARE_DATA
                 WHERE WARE_ID = %s
                 LIMIT 1
                 """
    
    row = cursor.execute(search_sql, id)
    return row


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

    if modified_amount < stock_range[0]:
        return 0
    elif modified_amount > stock_range[1]:
        return 0
    else:
        sql_data = [modified_amount, id]
        cursor.execute(update_sql, sql_data)
        db.commit()
        return 1


    def stock_display(table):
        db = function.connect_database()
        cursor = db.cursor()
        sql = '''
              SELECT * FROM WARE_DATA
              WHERE DATE_TIME > %s AND DATE_TIME < %s
              '''
        cursor.execute(sql, (startTime, endTime))
        results = cursor.fetchall()
        for i in results:
            row = table.rowCount()
            table.setRowCount(row + 1)
            date = i[0].strftime("%Y-%m-%d")
            table.setItem(row, 0, QTableWidgetItem(str(i[1])))
            table.setItem(row, 1, QTableWidgetItem(date))
            table.setItem(row, 2, QTableWidgetItem(str(i[2])))
            table.setItem(row, 3, QTableWidgetItem(str(i[3])))