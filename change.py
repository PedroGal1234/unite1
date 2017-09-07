#Pedro Gallino
#9/7/17
#change.py-tells you the number of coins that will make the amount of money

total = int(input('Eneter The Number of Cents: '))
quarters = total//25
print('Quarters: ',quarters)
dimes = (total-(quarters*25))//10
print('Dimes: ', dimes)
nickle = (total-(quarters*25)-(dimes*10))//5
print('Nickle: ', nickle)
penny =(total-(quarters*25)-(dimes*10)-(nickle*5))//1
print('Pennies: ',penny)