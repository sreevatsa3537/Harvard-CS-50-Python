import re
mail=input("Enter Your Email").strip()  #Removes leading and trailing whitespace
# So " test@gmail.com " becomes "test@gmail.com"

if re.search(r".+@.+\.com",mail):
# r"" Raw string Tells Python: “Don’t treat backslashes as escape characters”Without r, \. would mean "literal dot"
# so now this means .+ means "one or more of any character"@ means the literal @ character and again .+ means 
# "one or more of any character" \. means literal dot com means the literal characters "com" but for that r is must 
# . means any character except newline
# * means "zero or more" repititions 
# + means "one or more" repititions 
# ? means "zero or one" repititions 
# {m} means "exactly m" repititions 
# {m,n} means m-n repititions
    print("valid")
else:
    print("invalid")


