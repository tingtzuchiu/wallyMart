class Item():
    def __init__(self, name, tag, price, qty):
        self.name   =  name
        self.tag    =  tag
        self.price  =  price
        self.qty    =  qty

    def __str__(self):
        return "%s, %s,%s" %(self.name, self.price, self.qty)

    def get_name(self):
        return self.name

    def get_tag(self):
        return self.tag
    
    def get_price(self):
        return self.price

    def get_qty(self):
        return self.qty
