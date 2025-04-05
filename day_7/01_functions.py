# Functions

# A function is a block of code which only runs when it is called you can pass data, known as parameters, into a function.
# Funtions can return data as a result.
# In Python, a function is defined using the def keyword.

# Let's define a function
def greet_user():
    print("Hello, User!")

# calling a funtion
greet_user()

# defined a funtion
def aoa():
    print("Assalam o Alaekum, All the way from London")

# calling a function
aoa()

def aoa(name):
    print(f"Assalam o Alaekum, {name}! Kaifa Haluk?")

name = "Saifullah Khan"
#calling a funtion
aoa(name)

def aoa(name = "Meray Payaray Bhai"):
    print(f"Assalam o Alaekum, {name}! Kaifa Haluk?")

# calling a funtion
aoa("Saifullah")


# Return values
def square( number ):
    return number * number

# define a number
number = 14
result = square(number)
# called a function
print(result)

# Recursion

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial( n - 1 )

print(factorial(6))

# lambda funtion

def x(a):
    return a+2

x = lambda a: a + 10

print(x(5))

# two values lambda function

def x(a,b):
    return a*b

x = lambda a, b : a*b
print(x(2,8))