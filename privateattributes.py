class thisclass:
    __private = 27

    def __anonymousmethod(self):
        print("this a private/anonymous method is " +  thisclass.__anonymousmethod)
            
    def hello(self):
        print("the private value is", thisclass.__private)


one = thisclass()
one.hello()
