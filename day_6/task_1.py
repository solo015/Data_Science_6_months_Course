
#  Task#1
''' make a program where two persons are asking name and age to each other.
after age, make if condition to compare there age.
'''

name_a = input("What is your name?\n")
age_a = int(input("How old are you? \n"))

name_b = input("What is your name? \n")
age_b = int(input("How old are you?\n"))

# if elif else condition
if age_a > age_b : 
    print(name_b, "! I am older than you.")
elif age_a < age_b:
    print(name_b, "! You are older than me.")
else:
    print(name_b, "! Awesome we have same age.")

