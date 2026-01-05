class person:
    name="svj"
    age=45
    skill="python"
    def info(self): # method is a function that belongs to the class(Vo object jiskiliyae function call kr rhe h)
        # understand better:--it refers to the specific object currently calling the method.
        print (f"My Name is {self.name},age is {self.age},skill is {self.skill}")
a=person() # object creation and stored in variable a
a.info() # calling the method info using the object a
# method:--a function defined within a class that defines objects behaviour(actions) is called a method.
#Python secretly converts this to:  person.info(a)  So: self = a  Inside the method:


class student:
    def __init__(self,name,slno):# constructor
        self.name=name
        self.slno=slno
    def get_greetings(self):
        return f"Hello,Iam {self.name} and my serial number is {self.slno}"
s1=student("Svj",37)
s2=student("VCM",42)
print(s1.get_greetings()),print(s2.get_greetings())


class Device: 
# Constructor: initializes the unique state of the object 
    def __init__(self, serial_number): 
        self.serial_number = serial_number # Instance Attribute 
        self.is_on = False                
# State attribute 
# Method: Defines an action/behavior 
    def toggle_power(self): 
# The method uses 'self' to access and change the instance attribute 'is_on' 
        self.is_on = not self.is_on 
        status = "ON" if self.is_on else "OFF" 
        print(f"Device {self.serial_number} is now {status}.")
d=Device("X2 Pro")
d.toggle_power()  # Output: Device X2 Pro is now ON.
d.toggle_power()  # Output: Device X2 Pro is now OFF.



class Battery: 
    def __init__(self, charge_level): 
        self.level = charge_level 
         
    def report_charge(self): 
        return f"Battery is at {self.level}%."
def check_power(device_battery): 
    print("--- Power Check ---") 
    if device_battery.level < 20: 
        print("ALERT: Charge immediately!") 
    print(device_battery.report_charge())#"This function will receive something and I will call that something device_battery
car_battery = Battery(charge_level=95)
drone_battery = Battery(charge_level=15)
check_power(car_battery) # python will pass car_battery object to the function means device_battery will refer to car_battery
check_power(drone_battery) # python will pass drone_battery object to the function means device_battery will refer to drone_battery





























    



