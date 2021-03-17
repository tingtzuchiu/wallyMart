import sqlite3



class Track():
    def __init__(self):
        self.num     =  ''


    def set_num(self):
        set_tk       = input("What is your tracking number ? ")
        self.num     = set_tk
        return  self.num



    def check_status(self, num):
        konn        = sqlite3.connect('Order.db')
        a           = konn.cursor()
        alllines    = a.execute("select * from OrderList")
        package     = False
        for i in alllines:
            if i[4]  == num :
                print('Your package is in %s stage' %i[6])
                package = True

        if not package:  
            print('No Record! Please check your trackng number')

        a.close()
        

 
 
