import math
def cylinder_volume(height, radius=5):
    pi = 3.14159
    return height * pi * radius ** 2


cylinder_volume(10, 7)  # pass in arguments by position
cylinder_volume(height=10, radius=7)  # pass in arguments by name

print("###################")

# write your function here
def readable_timedelta(days):
    #week = math.floor(days/7)
    week = days // 7 # get int
    day = days%7
    return "{} week(s) and {} day(s).".format(week, day)

# test your function
print(readable_timedelta(10))


egg_count = 0
mynamess = "wwwwww"

def buy_eggs():
    print(egg_count)
    # mynamess[0] = "x"  #error
    mynamess = "xxxxxx" #ok
    print(mynamess)
    # egg_count += 12 # purchase a dozen eggs, can not modify, can read, rule for int and str

buy_eggs()


list = [1,2,3,4]

def addlist(newNum):
    ''' doc strings '''
    list.append(newNum)
    print(list)

addlist(5)








    
    
