# CSV means comma separated values It is used to store tabular data in plain text form its very useful
# with open("students.csv") as file:
#     for line in file:
#         name,house=line.rstrip().split(",") # split(",") method is used to split the string into list based on the separator provided 
#         # here separator is comma so it willl search for commas and where it finds one it will split the string into two parts
#         #and also here we are using two variables name and house to store the two parts of the string
#         print(f"{name} is in {house} house ") 
## MOre advanced code down below
students=[]
with open("students.csv") as file:
    for line in file:
        name,house=line.rstrip().split(",")
        student={"name":name,"house":house} # creating a dictionary to store the name and house of each student
        students.append(student) # appending the dictionary to the list of students
def get_name(student):
    return student["name"]  # function to get the name of the student from the dictionary

for student in sorted(students,key=get_name): # sorting the list of students based on the name using the get_name function
    print(f"{student['name']} is in {student['house']} house")
print(students)



# Question
# Write a Python program that reads student data from a CSV file named students.csv, 
# where each line contains a student's name and house separated by a comma.
# Your program should:
# Open and read the file.
# Store each student as a dictionary with keys "name" and "house".
# Append each dictionary to a list called students.
# Sort the list of students alphabetically by name.
# Print each student in the format:
# <name> is in <house> house
# Use a separate function to specify the sorting key.

students=[]
with open("students.csv") as file:
    for line in file:
        name,house=line.rstrip().split(",")
        student={"name":name,"house":house}
        students.append(student)

# def get_name(student):
#     return student["name"] Better way is to do with lambda function

for student in sorted(students,key=lambda student: student["name"]):
    print(f"{student["name"]} is in {student["house"]} house")
    
# another way when we have house adress also in csv file with a comma we import csv lib which is already coaded to handle such cases
import csv 
students=[]
with open("home.csv") as file:
    reader=csv.reader(file) # It will read the file and handle the commas in the data also
    for name,place in reader:
            # name,place=line.strip().split(",") This line is not needed as csv.reader already splits the data based on commas
        students.append({"name":name,"place":place})

for student in sorted(students,key=lambda s: s["name"]) : # Here sucker["name"] this means return 
    print(f"{student['name']} lives in {student['place']} ")

    








 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    