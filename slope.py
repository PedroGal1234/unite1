#Pedro Gallino
#9/1/17
#slope.py - Calculates slope after feeding in two points

x1 = float(input('x1: '))
y1 = float(input('y1: '))
x2 = float(input('x2: '))
y2 = float(input('y2: '))
slope = ((y2-y1)/(x2-x1))
print('Your slope is: ', slope)
print('The equation for your line is: y=',slope,'x+',(y1-(slope*x1)))