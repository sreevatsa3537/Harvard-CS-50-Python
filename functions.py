def hello(me):
    print("Hello to ",me) # defining the function here with parameter me

name=input("Enter your name:")
hello(name)  # calling the function here what is happenin is the value of name is passed to me parameter of hello function first we 
# gave the parameter me and then we called the function with argument name python assumes me === name here 

def defaultvalueofparameter(country="INDIA"):
    print("I am from ",country)
defaultvalueofparameter()




# Lets understand it deeply using return statement

def main():
    x = int(input("Enter first number: "))
    print("The square of the number is ",square(x)) # Here square(x) is calling the function square with argument x and the
    #value returned by square function is printed
    
def square(n):
    return n*n   # return statement is used to return the value from the function to the caller

main()