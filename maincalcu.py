#import calculadora.calculos as calc #alias

#print (calc.suma(2,3))

from calculadora.calculos import suma as sumar, resta as restar

print(sumar(2,3))
print(restar(2,3))