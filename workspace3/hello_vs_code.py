name = input("enter your name:")
print("hello there {}".format(name.title()))

try:
    num = int(input("entry num :"))
    print(num)
except:
    print("not availd num")

while True:
    try:
        xingming = float(input("entry float ...."))
        print(xingming)
        break
    except ValueError as e:
        print(" ValueError {}".format(e))
    except:
        print("not float ")
    finally:
        print("do finally ")

result = eval(input("input express ..."))
print(result)