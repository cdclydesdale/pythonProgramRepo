n = input('Enter number you want to find factorial of:')
val = int(n)
fact = 1
while(val>=1):
    fact = val * (val-1)

print(fact)
