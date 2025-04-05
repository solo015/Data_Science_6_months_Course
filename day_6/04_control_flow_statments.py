
# If conditions
# For loops

# Condition
"""
>
<
==
!=
"""
x = -10

# If elif else condition
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")

# For loops

# food list
menu = ["Dahi Bhallay", "Biryani", "Daal", "Samosay", "Tikiyan", "Shami", "Palak Paneer"]

# Loop
for item in menu:
    # separately displaying food items
    print(item)

# While loop

i = 1

while i < 11:
    print(i)
    # i = i + 1
    i+=1

# Control Break Statment
for letters in "Python":
    if letters == 'h':
        break
    print(letters)

# Control Continue Statment
for letters in "Python":
    if letters == 'h':
        continue
    print(letters)


# Control pass Statment
for letters in "Python":
    if letters == 'h':
        pass
    print(letters)




