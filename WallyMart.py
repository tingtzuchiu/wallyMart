
import datetime
import data_base as db
import Inventory as inv
import Item as it
import Payment as pay
import Order as order
import Review as rev
import Track as tk
import User as user
import random, string
import Screen as scr
import Merchant as mer


    
                
class WallyMart():
    def __init__(self):
        pass

    

    def Execute(self):
        a = db.Database()
        a.CreateDataBase()  # Link to Order db
    
        u = user.User()
        u.Create_user()     # Link to User db
    
        purchase  = []
        action    = 0
        login_lst = [False, '', '']
        screen    = scr.Screen()
        while True:
            try:
                action = int(input("Welcome to Wally mart!  \n 1.Login \n 2.Shopping \n 3.Cart \n 4.Reviews \n 5.Check status \n 6.Register \n 7.Goodbye! \nHow can we help you? "))
                if action >= 7:
                    raise NotValidOption
            except:
                print("Please make a valid choice! \n")
            

            if action == 1:
                if login_lst[0]:
                    print('-----------------------------------------------------')
                    print('You already login %s! Go back to main page ' %login_lst[1])
                    print('-----------------------------------------------------\n')
                    continue
                else:
                    login_lst  = screen.option1()            
            
            if action == 2:
                purchase = screen.option2()                         
                
            if action == 3:
                login_lst  = screen.option3(purchase,login_lst)
                purchase = []
            
            if action == 4:
                login_lst  = screen.option4(login_lst)
            
            if action == 5:
                screen.option5()

            if action == 6:
                login_lst  = screen.option6()

            if action == 7:
                print("Thank tou! see you again soon!")
                break

#WallyMart()
#a = WallyMart()
#a.Excecute()

    
        


