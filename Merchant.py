

import xlrd, xlwt

import xlutils.copy


class Merchant():

    def __init__(self):
        pass


    def add_item(self, cate, item, tag, price):
        wb    = xlrd.open_workbook('Inventory_list.xls', formatting_info=True)
        wc    = xlutils.copy.copy(wb)
        tab   = wb.sheet_names()
        count = 0
        valid = False
        
        for i in tab:
            count += 1
            if i == cate:
                valid = True
                break
            
        if not valid:
            # add sheet to workbook with existing sheets
            Sheet1 = wc.add_sheet(cate)
            wt     = wc.get_sheet(len(tab))
            wt.write(0, 0, 'Name')
            wt.write(0, 1, 'Tag')
            wt.write(0, 2, 'price')
            wt.write(1, 0, item)
            wt.write(1, 1, tag + '_' +  '1')
            wt.write(1, 2, price)          
            
            wc.save('Inventory_list.xls')
            #creat a new tab and write
            

        else:
            table   = wb.sheet_by_name(cate)
            num_row = table.nrows

            wt      = wc.get_sheet(count-1)

            wt.write(num_row, 0, item)
            wt.write(num_row, 1, tag + '_' +  str(num_row))
            wt.write(num_row, 2, price)
            wc.save('Inventory_list.xls')








'''
a = Merchant()  
a.add_item('Snack', 'ggg', 'S', 9.99)
a.add_item('Fresh', 'ttt', 'F', 6.99)
a.add_item('Fresh', 'andy', 'F', 2.99)
a.add_item('Snack', 'pai', 'S', 1.99)
a.add_item('Jordan', 'pai', 'J', 59)
a.add_item('Jordan', 'FFF', 'J', 123)
a.add_item('lEBRON', 'KKKK', 'D', 4.99)
'''
