import sys 

if len(sys.argv)>1000:
    sys.exit("Usage: python cmdline.py")



try:
    n=int(sys.argv[1])
except ValueError:
    sys.exit("Error: Argument must be an integer")

print(n**n)
    
    
