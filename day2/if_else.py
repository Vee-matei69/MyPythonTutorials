#prompt customer to enter consumption rate
consumption_rate = int(input('enter value of consumption rate: '))
kilometre_cover = int(input('enter value of kilometre to cover: '))

#amount of fuel to use
cost_litre = 180
amount_fuel = consumption_rate * kilometre_cover
total_cost = amount_fuel * cost_litre 
print('The amount of fuel to buy is; ', amount_fuel)
print('The total cost is; ', total_cost)

#conditions
if total_cost > 90000:
    print('Seems you have a long way to go. ')  
elif total_cost > 50000:
    print('A short journey mate!')  
else :
    print('You have no where to go.')
