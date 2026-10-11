class Account:
    def __init__(self,owner,pin):
        self.owner=owner
        self.__pin=pin
    def show_owner(self):
        print("account owner:",self.owner)
    def show_pin(self,entered_pin):
        if entered_pin==self.__pin:
            print("corrrect pin")
        else:
            print("incorrect pin")
account1=Account("arjun","1234")
account1.show_owner()
account1.show_pin("1234")


    
        