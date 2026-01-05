# there are types of errors that are not exceptions
# such as syntax errors, which occur at compile time
# but for ex take x = int(input("Enter a number: "))
# if the user enters a non-numeric value like "abc"
# it will raise a ValueError exception at runtime
# exceptions can be handled using try-except blocks

try:
    x = int(input("Enter a number: "))
    print(f"You entered: {x}")
except ValueError:
    print("That's not a valid number!")
# Another example 
try:
    x = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number!")
else:
    print(f"You entered: {x}")
# The print statement is outside the try-except block
# so if a ValueError occurs, x will not be defined it will raise a NameError
# To avoid this, we can initialize x before the try-except block or add an else block
# so basically when a string or stmg else is entered in try error occurs
# and except will print "thats not a valid number" and never lets x get defined it basically 
# skips x and python moves on to next pine i.e. print where the name error occurs cause x never got defined This will happen 
# if we dont use else block or initialize x before try-except block 

while True:
    try:
        x = int(input("Enter a number: "))
    except ValueError:
        print("That's not a valid number! Please try again.") # Here we can use ""pass"" if we dont want to print anything
        # loop will continue asking for input like same question again  
    else:
        break
print(f"You entered: {x}")
# This loop will keep asking for input until a valid integer is entered