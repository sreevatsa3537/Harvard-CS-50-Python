# A decorator is a special type of function in Python that modifies the behavior of another function,by taking it as an argument
# and returning a new function with enhanced functionality.
#   @decorater_function 
#   def my_func():
#       pass
# @ decorater_function is equivalent to my_func = decorater_function(my_func)

def greet(fx):# we pass in fx as an argument so here fx becomes hello as we are passing hello function to greet function
    # after @greet /n hello = greet(hello) is what happens internally as defined above
    def mfx(*args, **kwargs): # Very imp its called wrapper function it is used because to return the modified function if we dont do it 
        # then the original function will be lost;;; What happens when there is no wrapper function?
# This runs immediately when Python reads the fileNot when hello() is called And it returns None So this fails because:
# You executed the function too early You didn’t return a function to replace hello. Decorators must return a function. Always.
        print("good mrng")
        fx(*args, **kwargs) # calling the original function inside the wrapper function 
        # here *args and **kwargs are used to pass any number of arguments(x,y,z,a,b etc) 
        # *args stores any number of postional arguments as a tuple
        # **kwargs stores any number of keyword arguments as a dictionary 
        print("have a nice day")
    return mfx

@greet
def hello():
    print("hello world")
hello()

# @greet # use this or the line below
def add(x,y):
    print(x+y)        
(greet (add))(2,3)  # this will give error because mfx() like we did not say mfz(x,y) and it will become mfx(2,3) 
# which is wrong does not take any parameters so we need to use *args and **kwargs in mfx
# why we need both *args and **kwargs because if we have a function with both positional and keyword arguments
# def func(a,b,c=5,d=10): one cant do the job 