class cg:
    def __init__(self, level):
        self.level = level
def check_cg(b):
    print(f"charge is {b.level}")   # using object’s attribute
my_cg=cg(80)   # passing OBJECT instead of number
check_cg(my_cg)


class bank_acco:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self,amount):
        self.balance += amount
        print(f"Money Deposited {amount}. New balance is {self.balance}")
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Money Withdrawn {amount}. New balance is {self.balance}")
my_account=bank_acco("svj",10000)
my_account.deposit(5000)
my_account.withdraw(200)


class battery :
	def __init__(self,charge_level):
		self.charge_level=charge_level
	def report_charge(self):
		return f"Battery charge is {self.charge_level}"
def check_power(device_charge):
	if device_charge.charge_level < 20: #device_charge is not a number. It is a battery object. so we cant do device_charge <20
		print("Alert charge is less then 20%")
	print(device_charge.report_charge())
car_battery=battery(charge_level=96)
drone_battery=battery(charge_level=10)
check_power(car_battery)
check_power(drone_battery)


def file_dict(filename="marks.txt"):
    student_dict={}
    file = open(filename,"r")
    for line in file:
        line=line.strip()
        if ":" in line:
            name,marks=line.split(":")
            student_dict[name]=int(marks)
    file.close()
    return student_dict
result=file_dict()
print(result)

x=10
def fun():
    x=20
    print(x)
fun()
print(x)

try: 
    num1 = int(input("Enter numerator: ")) 
    num2 = int(input("Enter denominator: ")) 
    result = num1 / num2 
    print(f"Result: {result}") 
except ZeroDivisionError: 
    print("Error: Cannot divide by zero.")

def validate_age(age): 
    if age < 0 or age > 150: 
# Raise custom exception 
        raise ValueError(f"{age} is not a valid age") 
    return True 
# Caller code 
try: 
    validate_age(-5) 
except ValueError as e: 
    print(f"Caught an error: {e}")










