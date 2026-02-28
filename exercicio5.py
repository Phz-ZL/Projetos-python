#Declarar
a: float = 0
b: float = 0
c: float = 0
delta: float = 0
x1: float = 0.0
x2: float = 0.0

#Inicio
a = float(input('informe o valor do coeficiente a.'))
b = float(input('informe o valor do coeficiente b.'))
c = float(input('informe o valor do coeficiente c.'))
delta = (b**2)- (4*a*c)
x1 = (-b + delta**0.5)/(2*a)
x2 = (-b - delta**0.5)/(2*a)
print ('O valor de delta é: ', delta)
print ('O valor de X1 é:', x1)
print ('O valor de X2 é:', x2)
#Fim