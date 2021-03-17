
import re, wx, sqlite3, datetime, xlwt

class Database():
    def __init__(self):
        pass

    def CreateDataBase(self):
        konn = sqlite3.connect('Order.db')
        a = konn.cursor()
        a.execute("create table if not exists OrderList (username, name, adr, item, track, date, status)")
        konn.commit()
        

    def WriteIntoDB(self, l_visit):
        konn = sqlite3.connect('Order.db')
        # Open a cursor
        a = konn.cursor()

        # Add entries
        a.execute("insert into OrderList (username, name, adr, item, track, date, status) values (?, ?, ?, ?, ?, ?, ?)", \
                  (l_visit[0], l_visit[1], l_visit[2], l_visit[3], l_visit[4], l_visit[5], l_visit[6] ))
        konn.commit()

#[self.username, self.name, self.password,  self.adr, self.item, self.time, self.track, self.status]

    def ReadDataBase(self):
        konn = sqlite3.connect('Order.db')
        a = konn.cursor()

        alllines = a.execute("select * from OrderList")
        l_xl = []
        for i in alllines:
            l_xl.append(i)

        sort_l = sorted(l_xl, key = lambda x : x[5], reverse = True)

        for i in sort_l:
            print(i)
        a.close()



