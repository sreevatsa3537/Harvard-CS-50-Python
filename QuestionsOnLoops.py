def main():
    print_column(4)
    
def print_column(height):
    for i in range(height):
        print("#")
         
main()

print("__________________________________________________________")

def main():
    squares(3)

def squares(size):
    for i in range(size):
        for j in range(size):
            print("#",end="")
        print()

main()
# Q1: Why do we need print() inside the outer loop?
# Answer:
# Loops NEVER move to a new line automatically.
# The inner loop only prints characters on the same line because of end="".
# The outer loop prints one complete row of characters.
# After finishing a row, we must manually move to the next line.
# print() (with no arguments) tells Python: “Row finished — go to next line.”
# Therefore, the newline must be inside the outer loop, so it runs once per row.


# ✅ Q2: How does print() know when to move to the next line (after 3 characters)?
# Answer:

# print() does NOT know the number 3.
# The inner loop runs exactly 3 times because of range(3).
# After these 3 iterations, the inner loop finishes automatically.
# Only then does Python reach the print() line.
# So the newline happens after each full row, not after each character.
# The loop controls when the print() executes, NOT the print() itself.
# In short: newline happens after the inner loop completes its 3 prints.

#outer loop repeats the inner loop which tells to print in the same line by using end="" and the print() tells it to 
# go to the next line ;  after the inner loop is completed like print(# 3 times ) it will stop and go to the next 
# line which is print() which will move the cursor to the next line and the outer  loop runs the inner loop again 
# for the next row this happens 3 times because of range(size) in the outer loop.


print("__________________________________________________________")

def main():
    squares(4)
def squares(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)
main()

# This is another way of solving the same problem using a function to print a row

print("__________________________________________________________")
for i in range(3):
    print("#" * 3)
    
# This is most simplest way to print a square of # using multiplication operator means print("#" * 3) prints ### and the loop 
# repeats it 3 times because of range(3)