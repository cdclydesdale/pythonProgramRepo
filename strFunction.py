n = input('Enter number of words you would like to enter: ')
val = int(n)
alist = []
i = 1
for i in range(0,val):
    str = input('Enter word %i '%(i+1))
    alist.append(str) #Append can be used to add item to the end of the list

alist.sort()
print(alist)
