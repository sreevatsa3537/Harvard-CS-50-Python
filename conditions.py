marks = int(input("Enter marks: "))

if 0 <= marks <= 100: # Here we are checking if the entered marks are within a valid range
    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    elif marks >= 60:
        grade = "D"
    else:
        grade = "F"

    print("Grade:", grade)
else:
    print("Invalid marks entered!")



