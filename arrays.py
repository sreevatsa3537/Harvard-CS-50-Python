# Array in python is similar to list but it can only hold elements of the same data type.
# Arrays are more memory efficient than lists when dealing with large amounts of data of the same type
# import array as arr is we do this to avoid writing arr.array every time so we do 
# we have an table to store data of same type only
# 'b' -> signed char        (1 byte integer, can be negative)
# 'B' -> unsigned char      (1 byte integer, only positive)
# 'u' -> unicode character  (1 Unicode character)
# 'h' -> signed short       (2 byte integer, can be negative)
# 'H' -> unsigned short     (2 byte integer, only positive)
# 'i' -> signed int         (usually 4 bytes, can be negative)
# 'I' -> unsigned int       (usually 4 bytes, only positive)
# 'l' -> signed long        (usually 4 or 8 bytes, can be negative)
# 'L' -> unsigned long      (usually 4 or 8 bytes, only positive)
# 'f' -> float              (4 byte decimal number)
# 'd' -> double             (8 byte decimal number, more precise)

from array import * # importing everything from array module
val=array('i',[1,2,3,4,5]) # 'i' is type code for signed integer
print(val)
# we can use buffer_info() method to get the memory address and size of the array
print(val.buffer_info()) # returns a tuple (address, length)
# we can use typecode attribute to get the type of elements stored in the array
# we can indexing as usual and slicing reverse too
newarr=array(val.typecode,(a*a for a in val)) # creating new array using ((list comprehension)) first we have specify
# the typecode then we have given the expression
print(newarr)

## INput from user to create array
arr=array('i',[]) # empty array of signed integers
n=int(input("Enter number of elements: "))
for i in range(n):
    x=int(input("Enter element: "))
    arr.append(x) # appending elements to the array
print(arr)
v=int(input("Enter value to search: "))
k=0 # index variable
for i in arr:
    if i==v:
        print(k) # printing index of the element
        break
    k+=1
# OR we have index() method to find index of an element
print("Index of",v,"is",arr.index(v))
