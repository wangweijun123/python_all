points = 44  # use this as input for your submission

# establish the default prize value to None

prize = None
# use the points value to assign prizes to the correct prize names
result = "Congratulations! You won a {0}!"
if points <= 50:
    prize = "wooden rabbit"
elif points <= 150:
    result = "Oh dear, no prize this time."
elif points <= 180:
    prize = "wafer-thin mint"
else:
    prize = "penguin"

# use the truth value of prize to assign result to the correct prize
if prize:
    result = result.format(prize)

print(result)


score = 85;

if 0<=score<=40:
    print('low')
elif 40<score<=60:
    print('min')
elif 60<score<89:
    print('max')
else:
    print('super')
