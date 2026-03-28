class computer:
     def __init__(self):
           self.__maxprice = 500

     def sell(self):
           print("selling price = {}".format(self.__maxprice))      

     def set_maxprice(self, price):
           self.__maxprice = price

c = computer()
c.sell()

c = computer()
c.sell()

c = computer()
c.sell()

c.set_maxprice(600)
c.sell()
