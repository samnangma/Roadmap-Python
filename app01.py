
# first = int(input("Enter first number: "))
# second = int(input("Enter second number: "))
#
# sum = first + second
# print("Sum " +str(sum))

course = 'Python for Beginners'
print(course.upper())
print(course.lower())
print(course.find('n'))
print(course.replace('f','3'))
print('Python' in course)

x = 10
x = x + 3
x += 5
print(x)

y = 3 == 2

print(y)

price = 5
# and (both)
# or (at least one)
# not (reverse false to true )
print(price > 10 or price < 20)
print(not price > 10)

temperature = 25
if temperature > 30:
    print("It's a hot days")
    print("the temperature is greater than 30")
elif temperature < 30:
    print("It's a nice days")
elif temperature > 10:
    print("It's a cold day")
else:
    print("It's a pretty cold day")
print("Done")

weight = float(input("What is your weight? "))
unit = input("(K)g or (L)bs: ")

if unit.upper() == 'L':
    converted = weight * 2.20462  # Convert kg to lbs
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight / 2.20462  # Convert lbs to kg
    print("Weight in Kgs: " + str(converted))



