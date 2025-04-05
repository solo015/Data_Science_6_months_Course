
# Data Structure
# List
# Tuple
# Set
# Dictionary


# Define a list


# List of Food in string data type
food = ["Dahi Bhallay", "Biryani", "Daal", "Samosay", "Tikiyan", "Shami", "Palak Paneer"]

# displaying all items of 'food' list
print(food)

# indexing of list
print(food[0]) # Dahi Bhallay
print(food[1]) # Biryani
print(food[-1]) # Palak Paneer
print(food[-3]) # Tikiyan

# update the one item into another item
food[1] = "Chicken Pulao"

print(food[1])  # Chicken Pulao

print(food) # all item of food list

# 2 - Tuple
coordinates = (4.23, 9.34)

print(coordinates) # both values

print(coordinates[1]) # 9.29

# 3 - set
fruit_set = { "Banana", "mango", 'Apple', "melon", "Dates", "orange"}

print(fruit_set) # display all values

# adding the value
fruit_set.add("guava")

print(fruit_set) # updated items/values

# Dictionary {key: value}

car = { 'brand': "Ford", "Model": "Mustang", "year": 1964}

print(car) # displaying dictionary values

print(car['brand']) # Ford
print(car['model']) # Mustang
print(car['year']) # 1964

# updating the key value
car['year'] = 2023

print(car['year']) # 2023