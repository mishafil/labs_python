def boolean(a, b):
    check = False

    try:
        if a < 0 or b < 0:
            exit(1)

        elif b % a == 0:
            check = True
            return check

        else:
            return check
    except:
        print("Exception")

def simpleDigits(a, b):
    try:
        for i in range(a, b + 1):
            check = False
            if (i == 1) or (i % 2 == 0) or (i % 5 == 0 and i != 5):
                i += 1
            else:
                for j in range(2, i):
                    if boolean(j, i) == True:
                        check = True
                if check == False:
                    list.append(i)
        return list
    except:
        print("NoSimpleDigits")

list = []

a = int(input())
b = int(input())

print(boolean(a, b))
simpleDigits(a, b)
print(list)
