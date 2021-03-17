


class Payment():
    def __init__(self, name, address, num, exp):
        self.name    =  name
        self.address =  address
        self.num     =  num
        self.exp     =  exp
        self.valid   =  False

    def check_valid(self):
        if len(str(self.num)) == 5:
            self.valid = True
        return self.valid

 
 
