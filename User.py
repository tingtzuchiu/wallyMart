
import sqlite3

class User():
    
    def __init__(self):
        self.name      = ''
        self.password  = ''
        


    def Register(self):
        konn = sqlite3.connect('User.db')
        a = konn.cursor()
        alllines = a.execute("select * from UserList")
        user_list = []
        for i in alllines:
            user_list.append(i[0])   

        while True:
            name      =  input('Please create your username : \n')
            password  =  input('Please create your password : \n')

            if name in user_list:
                print('User name already exist! Please use another username: \n')
            else:                            
                a.execute("insert into UserList (username, password) values (?, ?)",(name, password ))
                konn.commit()
                break
        a.close()
        login = True

        return [login, name, password]


    def Create_user(self):
        konn = sqlite3.connect('User.db')
        a = konn.cursor()
        a.execute("create table if not exists UserList (username, password)")
        konn.commit()


    def Check_user(self):
        konn = sqlite3.connect('User.db')
        a = konn.cursor()
        alllines = a.execute("select * from UserList")
        user_dict = {}
        for i in alllines:
            user_dict[i[0]] = i[1]        
        a.close()
        return user_dict
