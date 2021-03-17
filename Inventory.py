
import xlwt, xlrd

class Inventory():
    def __init__(self):
        pass

    
    def Read(self,tab):
        wb    = xlrd.open_workbook('Inventory_list.xls')
        table = wb.sheet_by_name(tab)
        l     = [] 
        for rownum in range(1,table.nrows):
            l.append(table.row_values(rownum))
        return l
