str = "abcdefga"
strlen = len(str)
#d = dict(str)
#print(d)

lst = list(str)
#Create an empty dictionary
d = {}
x = 0
for x in range(strlen):
    d[x] = lst[x]

print(d)
