import pymysql
import function


class wares_data(object):
    def __init__(self, ware_id, name, amount, max_amount, min_amount, purchase_price, sell_price, unit, scale):
        # ATTENTION! Change the function before change the class attributes!
        db = function.connect_database()
        cursor = db.cursor()
        # data = [ware_id, name, amount, max_amount, min_amount, purchase_price, sell_price, unit, scale]
        self.ware_id = ware_id
        self.name = name
        self.amount = amount
        self.max_amount = max_amount
        self.min_amount = min_amount
        self.purchase_price = purchase_price
        self.sell_price = sell_price
        self.unit = unit
        self.scale = scale

        insert_sql = 'INSERT INTO WARE_DATA (ware_id,name,amount,max_amount,min_amount,purchase_price,sell_price,unit,scale) VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s")'\
                     % (ware_id, name, amount, max_amount, min_amount, purchase_price, sell_price, unit, scale)
        cursor.execute(insert_sql)
        db.commit()
        cursor.close()
        db.close()

    
    # alter functions are inefficient
    def alter_id(self, ware_id):
        self.ware_id = ware_id
    
    def alter_name(self, name):
        self.name = name
    
    def alter_amount(self, amount):
        self.amount = amount
    
    def get_data(self):
        # return_data = {}
        # return_data['name'] = self.name
        # return_data['amount'] = self.amount
        # return_data['description'] = self.description
        # How to get all the class attributes?
        return self.__dict__
    
    def print_attr(self):
        print(self.__dict__)


class stream_data(object):
    def __init__(self, ware_id, state, amount, left):
        pass


'''
def connect_database():
    # my_id = input('User Account: ')
    # my_password = input('Password: ')
    return pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='ctj20100030928',
                           database='supermarket')
'''


def test():
    db = function.connect_database()
    cursor = db.cursor()
    search_sql = 'SELECT * FROM WARE_DATA'
    cursor.execute(search_sql)
    results = cursor.fetchone()
    if results is None:
        print("查询为空")
    else:
        print(results)    
    cursor.close()
    db.close()


ware = wares_data(1, 'AKaga', 100, 1000, 1, 10, 100, 'kg', 100)
test()