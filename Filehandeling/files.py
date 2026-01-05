# names=[]
# for i in range(3):
#     name=input("Enter name: ")
#     names.append(name)
# for i in sorted(names):
#     print("Hello",i) This is classical way to take input and print sorted names
# Here we'll see how to do it in file handling

# file=open("names.txt","a") 
# # 'a' is used to append the data to the file 'w' is used to write the data to the file
# # and overwrite the existing data(remove existing data and write new data)
# file.write(name+"\n") # \n is used to go to next line after writing the name 
# file.close()
# Another way to write to a file using 'with' statement here we don't need to close the file explicitly
name=input("Enter name: ")
with open("names.txt","a") as file:
    file.write(name+"\n")

names=[]
with open("names.txt") as file:# when we say nothing it is by default read mode 
    for line in file:
        names.append(line.strip()) # strip() is used to remove the extra spaces and new line characters
for name in sorted(names,reverse=True):
    print("Hello",name)
