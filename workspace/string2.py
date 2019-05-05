str = "xx{0}"

print(str.format("yyyyy"))


points = 174  # use this input to make your submission
result = "Congratulations! You won a {0}!"

# write your if statement here
if points <= 50:
    result = result.format("wooden rabbit")
elif points <= 150:
    result = "Oh dear, no prize this time."
elif points <= 180:
    result = result.format("wafer-thin mint") 
elif points <=200:
    result = result.format("penguin")

print(result)


weight = 100;

height = 50

temp = weight / height**2
print(temp)


temp = weight / height*2
print(temp)

# 
errors = 3
if errors:
    print("You have {} errors to fix!".format(errors))
else:
    print("No errors to fix!")


    
