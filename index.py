
# a = input("What is your name? ")
# print("Hello " + a)

b="svj"
c="jj"
#print("hello",end="\n")   this is used to end the line with new line which is default behavior to put it in same line use end=""
print("hello",end=" ") # space indicates to put a space after hello 
print(b)
print("world",c,sep="---") # sep is used to separate the values with something else instead of space

# Format string or f string 
college = "harvard"
print(f"I'am studying in {college}")

#.strip() method is used to remove the extra spaces from starting and ending of the string
name = "   svj jjjj svj vv jj   ".strip().title()
print(name)
# print(name.strip())
# # .capitalize() method is used to convert the string into lowercase
# name2 = "sVJJJJJSFSVLSIBIUSB"
# print(name2.capitalize())
# #.title() method is used to convert the first letter of each word to uppercase
# name3 = "svj js js js"
# print(name3.title())


