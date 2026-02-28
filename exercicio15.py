#Declarar
c1: float = 0.0
c2: float = 0.0
h: float = 0.0

#Inicio
c1 = float(input('Informe o valor do primeiro cateto: '))
c2 = float(input('Informe o valor do segundo cateto: '))
h = ((c1 ** 2) + (c2 ** 2)) ** 0.5
print ('A hipotenusa do triângulo é: ', h)
#Fim