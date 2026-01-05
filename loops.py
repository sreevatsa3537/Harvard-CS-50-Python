i = 0
total = 0

while True:
    i = int(input("Enter a number (negative to stop): "))

    if i < 0:     # stop without adding
        break

    total = total + i
    print(f"Current total is: {total}")

print(f"Final total is: {total}")
# This code continuously prompts the user to enter numbers and adds them to a total.
# It stops when a negative number is entered, without adding that negative number to the total.



# def meow():
#     while True:
#         n=int(input("Enter a number "))
#         if n>0:
#             break
#     for i in range(n):
#         print(meow_sound())
# def meow_sound():
#     return "Meow!"
# meow()

while True:
    n = int(input("Enter a positive number: "))
    if n > 0:
        break
    for i in range(n):
        print("Meow!")  # Same as above but simplified without a separate function