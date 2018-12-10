import pymysql


class wares_data(object):
    def __init__(self, ware_id, name, amount, max_amount, min_amount, purchase_price, sell_price, unit, scale):
        # ATTENTION! Change the function before change the class attributes!
        self.ware_id = ware_id
        self.name = name
        self.amount = amount
        self.max_amount = max_amount
        self.min_amount = min_amount
        self.purchase_price = purchase_price
        self.sell_price = sell_price
        self.unit = unit
        self.scale = scale
    
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
