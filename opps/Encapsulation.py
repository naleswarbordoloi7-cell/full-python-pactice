# Encapsulation = Data Hiding+ data protection
class Bankaccount:
    def __init__(self,balance):
        self.__balance =balance

    def set__balance(self,amount):
         self.__balance =amount
    
    def get_balance(self):
        return self.__balance
    
account = Bankaccount(150)
account.set__balance(100)
print(account.get_balance())



# bank account
class  Bankaccount:
    def __init__(self,balance):
        self.__balance=balance

    def deposit(self,amount):
        self.__balance+=amount
        
    def withdraw(self,amount):
        if amount <=self.__balance:
            self.__balance-= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance
    
account = Bankaccount(10000)

account.deposit(2000)
account.withdraw(3000)

print("balance:",account.get_balance())


class encapsulation:
    def __init__(self,value):
        self.__private_value =value
    def get_value(self):
        return self.__private_value
    def set_value(self,new_value):
        if new_value >=0:
            self.__private_value = new_value
demo = encapsulation(10)
print(demo.get_value())
demo.set_value(20)
print(demo.get_value())


class areacalulaor:
    def areaofcircle(self,r):
        area = 3.14 + r ** 2
        return area
    def areaofrectringle(self,l,b):
        area = l * b
        return area
calc = areacalulaor()
print(calc.areaofcircle())
calc.areaofcircle()
print(calc.areaofrectringle())
calc.areaofrectringle()



