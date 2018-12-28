str = input('Enter an input string')
strLen = len(str)
lst = list(str)

lst2 = []
x = 0

while x < strLen:
    for x in range(strLen):
        if x%2 == 0:
            #Insert into list/dictionary
            lst2.append(lst[x])
            x+=1
            #print(lst[x])
        else:
            pass

print('The String is ',lst2)
