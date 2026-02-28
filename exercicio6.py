#Declarar
x: float = 0.0
y: float = 0.0
z: float = 0.0

#Inicio
x = float(input('Informe o valor de X. '))
y = float(input('Informe o valor de Y. '))
z = x
x = y
y = z
print('O valor de X agora é', x)
print('O valor de Y agora é', y)
#Fim