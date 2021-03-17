import datetime
import xlrd, xlwt
import data_base as db
import Item as it

class Order(db.Database, it.Item):
    def __init__(self, username, name, password, adr, item, track):
        self.username  = username
        self.name      = name
        self.password  = password 
        self.adr       = adr
        self.item      = item
        self.time      = datetime.datetime.today()
        self.track     = track
        self.status    = 'Initial'
        


    def __str__(self):
        return "%s,%s,%s,%s,%s,%s" %(self.username, self.name, self.password,  self.adr, self.item, self.time)
        
    def Return_info_list(self):
        item_str = ''
        count = 0
        for i in self.item:
            if count < len(self.item) -1:
                item_str += '[ %s, %s, %s, %s ], ' %(i.get_name(), i.get_price(), i.get_tag(), i.get_qty())
                count +=1
            else:
                item_str += '[ %s, %s, %s, %s ] ' %(i.get_name(), i.get_price(), i.get_tag(), i.get_qty())
        return [self.username, self.name, self.adr, item_str, self.track, self.time, self.status]
