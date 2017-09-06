#Pedro Gallino
#9/6/17
#additionGameDemo.py- our first "game"

from random import randint
num1 = randint(1,10)
num2 =randint(1,10) 
awnser = int(input((str(num1))+ '+'+str(num2)+' = '))
print(awnser== num1 + num2)

