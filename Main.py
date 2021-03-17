
import datetime
import data_base as db
import Inventory as inv
import Payment as pay
import Order as order
import Review as rev
import Track as tk
import User as user
import random, string
import Screen as scr
import Merchant as mer
import WallyMart as wm

               
###################################################################################################
###################################################################################################

###  Main

###################################################################################################
###################################################################################################


while True:
    a = int(input(' 1. Customer \n 2. Merchant \n 3. Quit \nPlease verify your identity: \n '))

    if a == 1:
        action = wm.WallyMart()
        action.Execute()

    if a == 2:
        cate  = input('What Category you would like to add : \n')
        item  = input('What Item you would like to add : \n')
        tag   = input('What is the tag for this item : \n')
        price = input('What the price for the item you add : \n')
        g = mer.Merchant()
        g.add_item(cate, item, tag, price)
    if a== 3:
        print('-------------------------------------------')
        print('Thanks for using !!! Goodbye')
        print('-------------------------------------------\n')
        break
    
        


