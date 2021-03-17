
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

class NotValidOption(Exception):
    pass
    


class Screen():

    def __init__(self):
        pass

    def num_check(self):
        while True:
            try:
                num = int(input("Please enter credit card number!  \n"))
            except:
                print('-------------------------------------')
                print("Please enter digit only ")
                print('-------------------------------------\n')
                continue
            break
        return num

    def option1(self):
        while True:
            name      = input("Please enter your user name: \n")
            password  = input("Please enter your password: \n")
            login     = False
            u         = user.User()
            dict_user = u.Check_user()
            if name in dict_user:
                if dict_user[name] == password:
                    print("Welcome back %s !" %(name))
                    login = True
                    break
                else:
                    print("Wrong password")

            else:
                print("User doesn't exist! Please register first")
                break
        return [login, name, password]

#######################################################################
    def option2(self):
        buy_list = []
        while True:
            try:
                shopping = int(input(" 1.Fresh \n 2.Kitchen \n 3.Bath \n 4.Snack \n 5.Check out \nPlease select a category!  \n"))
                if shopping > 5:
                    raise NotValidOption
            except:
                print('-------------------------------------')
                print("Please make a valid choice! ")
                print('-------------------------------------\n')
                continue

            if shopping == 1:
                category  =  'Fresh'
            if shopping == 2:
                category  =  'Kitchen'
            if shopping == 3:
                category  =  'Bath'
            if shopping == 4:
                category  =  'Snack'
            if shopping == 5:
                break

            a = inv.Inventory()
            show_list  =  a.Read(category)
            print("Please select from below items :")
            for index , item in enumerate(show_list):
                print(str(index) ,':', item[0],', Price :', item[2])

            sel = int(input('Please select Item you like ? \n'))
            qty = int(input('How many sets would you like ? \n'))

            try:
                if sel >= len(show_list):
                    raise NotValidOption
            except:
                print('-------------------------------------')
                print("Item you select does not exist! ")
                print('-------------------------------------\n')
                print('-------------------------------------')
                print('Return to Category page')
                print('-------------------------------------\n')
                continue

            item = it.Item(show_list[sel][0], show_list[sel][1], show_list[sel][2],  qty)
            buy_list.append(item)
            print('-------------------------------------')
            print('Go Back to Category page')
            print('-------------------------------------\n')
        return buy_list
    
#######################################################################
    def option3(self, purchase, login):
        while True:
            try:
                cart = int(input(" 1.Review Order \n 2.Check out \n What would like to do?  \n"))
                if cart > 3:
                    raise NotValidOption
            except:
                print('-------------------------------------')
                print("Please make a valid choice! ")
                print('-------------------------------------\n')
                continue
            if cart == 1:
                print("You have below item in your cart:")
                for i in purchase:
                    print(i.get_name(), 'x',i.get_qty(), 'Price:', i.get_qty()* i.get_price())
                continue
                
            if cart == 2:
                total = 0
                if login[0] :
                    #total = 0
                    for i in purchase:
                        total += i.get_qty()* i.get_price()
                    print("Total Cost : %s" %total)
                    if total == 0:
                        print('-----------------------------------------')
                        print("Your cart is empty! Go back to main page")
                        print('-----------------------------------------\n')
                    else:    
                        while True:
                            shipping_adr   = input('Please enter your shipping address : \n')
                            credit_name    = input('Please enter your name on card : \n')
                            credit_num     = self.num_check()
                            credit_exp     = input('Please enter exp date on card (mm/yy) : \n')
                            credit_info    = pay.Payment(credit_name, shipping_adr, credit_num, credit_exp)
                            if credit_info.check_valid():
                                track_str  = ''.join(random.sample(string.ascii_letters + string.digits, 8))
                                my_order   = order.Order(login[1], credit_name, login[2], shipping_adr, purchase, track_str)
                                my_order.WriteIntoDB(my_order.Return_info_list())
                                print('------------------------------------------------------------')
                                print("Your order is Complete! %s is your tracking number" %track_str)
                                print('-----------------------------------------------------------\n')
                                break
                            else:
                                print('-------------------------------------')
                                print("Please check your credit card info")
                                print('-------------------------------------\n')
                                
#                    break  # Use to break option3 while loop
                else:
                    print("Please login:")
                    result = self.option1()
                    login  = result
                    for i in purchase:
                        total += i.get_qty()* i.get_price()
                    print("Total Cost : %s" %total)
                    if total == 0:
                        print('-----------------------------------------')
                        print("Your cart is empty! Go back to main page")
                        print('-----------------------------------------\n')
                    else:
                        continue
    
            return login
#######################################################################
    def option4(self, login):
        while True:
            try:
                review = int(input(" 1.Write a review \n 2.Check most recent review \n What would like to do?  \n"))
                if review > 3:
                    raise NotValidOption
            except:
                print('-------------------------------------')
                print("Please make a valid choice! ")
                print('-------------------------------------\n')
                continue


            if review == 1:       
                if not login[0] :   #True no need to enter info
                    print('Please Login :')
                    login = self.option1()

                feedback = input("Please give us some feedback based on your recnt purchase : \n")

                result = rev.Review(login[1], feedback)
                result.Submit()
                print('---------------------------------------------')
                print("Thanks for your feedback! Go back to Main Page")
                print('---------------------------------------------\n')
                break

            if review == 2:
                rev.Review.Show_Review()
                break
        return login
#######################################################################
    def option5(self):
        track   = tk.Track()
        track.check_status(track.set_num())
        print('-------------------------------------------')
        print("Go back to Main Page")
        print('-------------------------------------------\n')



#######################################################################
    def option6(self):
        login     = False
        u         = user.User()
        user_lst  = u.Register()
        return user_lst

    
#######################################################################
#######################################################################
#######################################################################
#######################################################################
#######################################################################

