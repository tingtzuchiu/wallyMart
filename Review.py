
import sqlite3
import datetime

class Review():
    def __init__(self, name, feedback):
        self.name      = name
        self.feedback  = feedback

    def get_feedback(self):
        return self.feedback

    def Submit(self):
        konn = sqlite3.connect('Review.db')
        a = konn.cursor()
        a.execute("create table if not exists ReviewList (username, review, date)")
        a.execute("insert into ReviewList (username, review, date) values (?, ?, ?)", \
                  (self.name, self.feedback, datetime.datetime.today()))
        konn.commit()
        pass

    def Show_Review():            
        konn = sqlite3.connect('Review.db')
        a = konn.cursor()

        alllines = a.execute("select * from ReviewList")
        l_xl = []
        for i in alllines:
            l_xl.append(i)

        num  = int(input('How many review would you like to show ?'))

        sort_l = sorted(l_xl, key = lambda x : x[2], reverse = True)

        if num > len(sort_l):
            num = len(sort_l)
        
        print("Show %s most recent Review" %num)
        for i in range(num):
            print(sort_l[i])
        a.close()
    



