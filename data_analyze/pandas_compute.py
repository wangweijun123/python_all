import pandas as pd
import numpy as np

# We create a Pandas Series that stores a grocery list of just fruits
fruits = pd.Series(data=[10, 6, 3], index=['apples', 'oranges', 'bananas'])

# We print fruits for reference
print('Original grocery list of fruits:\n ', fruits)

# We perform basic element-wise operations using arithmetic symbols
print()
print('fruits + 2:\n', fruits + 2)  # We add 2 to each item in fruits
print()
print('fruits - 2:\n', fruits - 2)  # We subtract 2 to each item in fruits
print()
print('fruits * 2:\n', fruits * 2)  # We multiply each item in fruits by 2
print()
print('fruits / 2:\n', fruits / 2)  # We divide each item in fruits by 2
print()

# We import NumPy as np to be able to use the mathematical functions
import numpy as np

# We print fruits for reference
print('Original grocery list of fruits:\n', fruits)

# We apply different mathematical functions to all elements of fruits
print()
print('EXP(X) = \n', np.exp(fruits))
print()
print('SQRT(X) =\n', np.sqrt(fruits))
print()
print('POW(X,2) =\n', np.power(fruits, 2))  # We raise all elements of fruits to the power of 2

# We print fruits for reference
print('Original grocery list of fruits:\n ', fruits)
print()

# We add 2 only to the bananas
print('Amount of bananas + 2 = ', fruits['bananas'] + 2)
print()

# We subtract 2 from apples
print('Amount of apples - 2 = ', fruits.iloc[0] - 2)
print()

# We multiply apples and oranges by 2
print('We double the amount of apples and oranges:\n', fruits[['apples', 'oranges']] * 2)
print()

# We divide apples and oranges by 2
print('We half the amount of apples and oranges:\n', fruits.loc[['apples', 'oranges']] / 2)
print('Original grocery list of fruits:\n ', fruits)
print()

# We multiply our grocery list by 2
print(fruits * 2)

#################### 练习 ##############


distance_from_sun = [149.6, 1433.5, 227.9, 108.2, 778.6]

planets = ['Earth', 'Saturn', 'Mars', 'Venus', 'Jupiter']

dist_planets = pd.Series(data=distance_from_sun, index=planets)
time_light = dist_planets.values / 18
print()
print(time_light)

print()
time_light = dist_planets / 18
print(time_light)

print()
print(time_light[time_light < 40])

# x = np.array([1, 2, 3, 4])
# print(x[x < 2])
