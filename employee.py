"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract, commission):
        self.name = name
        self.contract = contract
        self.commission = commission

    def get_pay(self):
        total = self.contract.calcAmount()
        if self.commission!=None:
            total+=self.commission.calcAmount()
        return total

    def __str__(self):
        msg=""
        if(self.contract.type=="Salary"):
            if(self.commission==None):
                msg = (f"{self.name} works on a monthly salary of {self.contract.calcAmount()}.  Their total pay is {self.get_pay()}.")
            elif(self.commission.type=="Fixed"):
                msg = (f"{self.name} works on a monthly salary of {self.contract.calcAmount()} and receives a bonus commission of {self.commission.calcAmount()}.  Their total pay is {self.get_pay()}.")
            elif(self.commission.type=="Variable"):
                msg = (f"{self.name} works on a monthly salary of {self.contract.calcAmount()} and receives a commission for {self.commission.contracts} contract(s) at {self.commission.rate}/contract.  Their total pay is {self.get_pay()}.")
            else:
                msg = ("Something has gone wrong at commission 1!")
        elif(self.contract.type=="Hourly"):
            if(self.commission==None):
                msg = (f"{self.name} works on a contract of {self.contract.hours} hours at {self.contract.rate}/hour.  Their total pay is {self.get_pay()}.")
            elif(self.commission.type=="Fixed"):
                msg = (f"{self.name} works on a contract of {self.contract.hours} hours at {self.contract.rate}/hour and receives a bonus commission of {self.commission.calcAmount()}.  Their total pay is {self.get_pay()}.")
            elif(self.commission.type=="Variable"):
                msg = (f"{self.name} works on a contract of {self.contract.hours} hours at {self.contract.rate}/hour and receives a commission for {self.commission.contracts} contract(s) at {self.commission.rate}/contract.  Their total pay is {self.get_pay()}.")
            else:
                msg = ("Something has gone wrong at commission 2!")
        else:
            msg = ("Something has gone wrong at contract!")
        return msg

class Contract:
    def __init__(self, type):
        self.type = type

class Commission:
    def __init__(self,type):
        self.type = type

class SalaryContract(Contract):
    def __init__(self,type,amount):
        super().__init__(type)
        self.amount = amount

    def calcAmount(self):
        return self.amount


class HourlyContract(Contract):
    def __init__(self,type,hours,rate):
        super().__init__(type)
        self.hours = hours
        self.rate = rate

    def calcAmount(self):
        return (self.hours*self.rate)

class FixedCommission(Commission):
    def __init__(self,type,bonus):
        super().__init__(type)
        self.bonus = bonus

    def calcAmount(self):
        return self.bonus


class VariableCommission(Commission):
    def __init__(self,type,contracts,rate):
        super().__init__(type)
        self.contracts = contracts
        self.rate = rate

    def calcAmount(self):
        return (self.contracts*self.rate)


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
bContract = SalaryContract("Salary", 4000)
billie = Employee('Billie', bContract, None)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
cContract = HourlyContract('Hourly', 100, 25)
charlie = Employee('Charlie', cContract, None)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
rContract = SalaryContract('Salary', 3000)
rCommission = VariableCommission('Variable', 4, 200)
renee = Employee('Renee', rContract, rCommission)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jContract = HourlyContract('Hourly', 150, 25)
jCommission = VariableCommission('Variable', 3, 220)
jan = Employee('Jan', jContract, jCommission)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
roContract = SalaryContract('Salary', 2000)
roCommission = FixedCommission('Fixed', 1500)
robbie = Employee('Robbie',roContract, roCommission)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
aContract = HourlyContract('Hourly', 120, 30)
aCommission = FixedCommission('Fixed', 600)
ariel = Employee('Ariel', aContract, aCommission)

print(str(billie)=="Billie works on a monthly salary of 4000.  Their total pay is 4000.")
#print(str(billie))
#print(billie.__str__())
#print(charlie.__str__())
#print(renee.__str__())
#print(jan.__str__())
#print(robbie.__str__())
#print(ariel.__str__())
