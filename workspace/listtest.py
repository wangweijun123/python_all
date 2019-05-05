# iterable of cities
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

# for loop that iterates over the cities list
for city in cities:
    print(city.title())

print('###########3')
for index in range(len(cities)):
    if (index == 2):
        break;
    print(index)
    print(cities[index])
print('###########3')



list = range(4)
print(list)

for l in list:
    print(l)


for l in list:
    print(l)



cities = ['bj', 'sh', 'zj']

capitalized_cities = [city.title() for city in cities]

print(capitalized_cities)

squares = [x**2 for x in range(9) if x % 2 == 0]

print(squares)


names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.title().lower() for name in names]
print(first_names)

multiples_3 = [item for item in range(21) if item>0]
print(multiples_3)

multiples_3 = [item*3 for item in range(21) if item>0]
print(multiples_3)




passed = []# write your list comprehension here
print(passed)



names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.split()[0].lower() for name in names]
print(first_names)


myname = 'wang xiankukn'
print(myname.split())


