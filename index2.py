# split function is used to split the string into list of words based on space or any other separator
name = input("Enter your full name: ").strip().title()
first,last = name.split(" ")# splitting based on space it wont work if we give too much space or no space 
print(f"Your first name is {first} and last name is {last}")