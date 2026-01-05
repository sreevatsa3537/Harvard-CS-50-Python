def main():
    x = int(input("Enter a number: "))
    if even(x):
        print(x, "is even")
    else:
        print(x, "is odd")
        
def even(n):
    return n % 2 == 0 # or can be done in if else statements also 
    
    
main()
    