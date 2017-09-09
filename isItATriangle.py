#Pedro Gallino
#9/7/17
#isItATriangle.py- find out if a thing is a triangle

a = float(input('Enter Side A: '))
b = float(input('Enter Side B: '))
c = float(input('Enter Side C: '))

short = min(a,b,c)
long = max(a,b,c)
medium = (a+b+c)-(short+long)

print((short+medium)>long)
