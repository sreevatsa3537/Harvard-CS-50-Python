count=0
with open("data.txt","r") as file:
    for line in file:
        count+=1
print("Number of lines:",count)


try: 
    num1 = int(input("Enter numerator: ")) 
    num2 = int(input("Enter denominator: ")) 
    result = num1 / num2 
    print(f"Result: {result}") 
except ZeroDivisionError: 
    print("Error: Cannot divide by zero.")
