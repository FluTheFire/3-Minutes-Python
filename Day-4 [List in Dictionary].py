# Create dictionary 
car = {'Honda':['civic','accord','jazz'], 'Toyota':{1:'vios', '2': 'yaris'}}

# print list in dictionary
print(car['Honda'])
# print list[index] in dictionary
print(car['Honda'][1])
# print dictionary in dictionary
print(car['Toyota']['2'])

# print type of car (car type)
print(type(car))
# print keys of dictionary car
print(car.keys())

# Create variable 
# variable is list of car.keys()
brand = list(car.keys())
print(brand)

# car.values() is value in dictionary car
# print list of car.values()
print(list(car.values()))

# car.items() is items in car
# print list of car.items()
print(list(car.items()))
