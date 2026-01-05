import csv
names=[]
with open("dictread.csv") as file :
    reader= csv.DictReader(file)
    for row in reader:
        names.append({"name":row["name"],"city":row["city"]})
        # Everything under the name column goes into row["name"] and here row is a new dictionary created for each key value pair 
        # Everything under the city column goes into row["city"]

for student in sorted(names,key=lambda s:s["name"]):
    print(f"{student['name']} is in {student['city']} city")
    
# Now We'll see how to insert csv files 
import csv
name=input("Enter name: ")
age=input("Enter age: ")
city=input("Enter city: ")
with open("insert.csv","a",newline="") as file:# newline="" is used to avoid extra blank lines in between the rows
    writer=csv.DictWriter(file, fieldnames=["name", "age", "city"]) # fieldnames is used to specify the column names
    writer.writerow({"name": name, "age": age, "city": city}) # A dictionary is always made of key-value pairs.
# Example: {"key": value}
# Keys are labels (usually strings), values are the actual data.
# So "name": name means:
#   "name" -> dictionary key
#   name -> variable holding the value

# writerow functions below:--
# Writes one row into the CSV file.
# The list represents the columns in that row.
# Example: ["Arjun", "19", "Delhi"] becomes:
# Arjun,19,Delhi
# The CSV writer automatically handles commas and newlines.
