#prompt customer to enter consumption rate
consumption_rate = int(input('enter value of consumption rate: '))
kilometre_cover = int(input('enter value of kilometre to cover: '))

#amount of fuel to use
cost_litre = 180
amount_fuel = consumption_rate * kilometre_cover
total_cost = amount_fuel * cost_litre 
print('The amount of fuel to buy is; ', amount_fuel)
print('The total cost is; ', total_cost)
