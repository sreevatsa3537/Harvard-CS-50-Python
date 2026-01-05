students={
    "Harry":"Gryffindor",
    "Ron":"Gryffindor",         
    "Hermione":"Gryffindor",
    "Draco":"Slytherin"
}   

for student in students :
    print(student,students[student],sep=", ")
    
print("____________________________________________________________________") 


students=[  # Here we have craeted  a list of dictionaries
    {"name":"Harry","house":"Gryffindor","mentor":"otter"},
    {"name":"Ron","house":"Gryffindor","mentor":"stag"},
    {"name":"Hermione","house":"Gryffindor","mentor":"jack"},
    {"name":"Draco","house":"Slytherin","mentor":None}
]

for student in students:
    print(student["name"],student["house"],student["mentor"],sep=", ")