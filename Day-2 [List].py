# TODO Create List
car = []

# TODO Add Object in List
car.append('Honda')
car.append('Toyota')
car.append('Yamaha')

print(car)              # Output: ['Honda', 'Toyota', 'Yamaha']

# TODO Delete Object in List
car.remove('Yamaha')

print(car)              # Output: ['Honda', 'Toyata']

print(car[0])           # Output: Honda

# TODO [V.2] Delete Object in List 
del car[0] # del ย่อมาจาก delete

print(car)              # Output: ['Toyota']

car.append('Suzukiiii')

print(car)              # Output: ['Toyota', 'Suzukiiii']

# TODO Edit Object in List
car[1] = "Suzuki"

print(car)              # Output: ['Toyota', 'Suzuki']





