name = input("Enter your name ")
# Instead of if else we can also use match function as follows 
match name:
    case "Harry" | "Hermonie" | "Ron":
        print("Gryfindor")
    case "Draco":
        print("Slytherine")
    case _: # MEans any out put except the above mentioned 
        print("Who are you")
