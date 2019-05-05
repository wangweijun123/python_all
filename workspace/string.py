s = 'udacity'
up = s.upper()
print up
print up[0]

print up[0] + s[1:]



def median(a,b,c):
    if a > b:
        if b > c:
            return b
        else:
            if a > c:
                return c
            else:
                return a
    else:
        if b < c:
            return b
        else:
            if a < c:
                return c
            else:
                return a


print median(2,3,3)


def getlast(s, tar):
    lastp = -1
    temp = 0
    while True:
       temp = s.find(tar,lastp+1)
       if temp == -1:
           break;
       lastp = temp
    print lastp
    
getlast('abcaaca', 'a')


def replaceStr():
    str = "xx{0}"
    str.format("yyyyy")






        
