class computer:
     def __init__(self):
           self.__minprice = 500
           self.__maxprice = 2000
           self.midprice = 1000

     def sell(self):
           print("selling price = {}".format(self.__minprice))      

     def sellmax(self):
           print("selling price = {}".format(self.__maxprice))      

     def sellmid(self):
           print("selling price = {}".format(self.midprice))

     def set_minprice(self, price):
              self.__minprice = price

     def set_maxprice(self, price):
              self.__maxprice = price

c = computer()
print("normal everday use laptop")
c.sell()
print("intel core i7 14th gen g5,16gb ram,512gb ssd,intel iris xe graphics")


c = computer()
print("business class laptop")
c.sell()
print("amd ryzen 7 7735u,16gb ram,512gb ssd,amd radeon graphics")

c = computer()
print("creators laptop")
c.sellmid()
print("intel core i9 14th gen H,32gb ram,1tb ssd,nvidia rtx 4070 graphics,pen support")

c = computer()
print("high end but light gaming laptop")
c.sell()
print("intel core i9 14gen h, 64gb ram, 1tbssd nivida 5070 graphics,good and light cooling system")