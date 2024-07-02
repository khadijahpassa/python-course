cars = ["Honda", "Volvo", "Hyundai", "Toyota"]
print(cars)
print(type(cars))
print(len(cars))

# Get value
print(cars[1])
print(cars[2])
print(len(cars[-1]))

# Add item
cars.append("Tesla")
print(cars)

# Change item
cars[1] = "BMW"
print(cars)

# Remove item
cars.remove("Toyota")
print(cars)

# Clear all item
cars.clear()
print(cars)

print("List Constructor")

fruits = list(("Durian", "Apple", "Melon"))
print(fruits)
print(type(fruits))

text = "Alhazen"
text_list = list (text)
print (text_list)
print (type(text_list))

text = "Alhazen"
text_list = list( (text,))
print (text_list)
print (type (text_list))