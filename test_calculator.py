# -------------------------------
# What is __name__ in Python?
# -------------------------------
# When Python runs a file, it automatically creates a variable called __name__.
# This variable tells the file HOW it is being used.

# Two possibilities:
# 1. If the file is RUN directly:
#       python file.py
#    Then:
#       __name__ = "__main__"
#
# 2. If the file is IMPORTED in another file:
#       import file
#    Then:
#       __name__ = "file"        # (the module's name)


# -------------------------------
# Why use __name__ == "__main__" ?
# -------------------------------
# We use it to control which code runs automatically.
# Code inside this block ONLY runs when the file is executed directly.
# It does NOT run when the file is imported as a module.

# Example:
# def main():
#     print("Running main program")

# if __name__ == "__main__":
#     main()

# If run normally:
#   python file.py
# Output:
#   Running main program
#
# If imported:
#   import file
# Output:
#   (nothing happens automatically)


# -------------------------------
# Practice Example
# -------------------------------
# def hi():
#     print("hello")

# if __name__ == "__main__":
#     print("run me")

from calculator import square
def main():
    test_square_positive()
    test_square_negative()
    test_square_zero()
def test_square_positive():
    assert square(2) == 4 # Assert is used to strictly say that the value should be equal to this if its not 
    # Then we'll get an AssertionError
    assert square(3) == 9
    assert square(4) == 16
def test_square_negative():
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(-4) == 16
def test_square_zero():
    assert square(0) == 0
# When we run """python -m pytest test_calculator.py """ it will automatically detect the functions
# starting with test_ and run them for testing so to test our file name has to begin with 
#test_*** or we'll target specific part in our file 