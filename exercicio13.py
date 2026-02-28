#Declarar
kg: float = 0.0
g: float = 0.0
Dias: float = 0.0

#Inicio
kg =float(input('Me informe quantos quilos de alimento comprado: '))
g = 1000 * kg
Dias = g / 50
print ('Consumindo 50g por dia, seu alimento vai durar por ', Dias, 'dias')
#Fim