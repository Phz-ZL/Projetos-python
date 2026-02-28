#Declarar
dist: float = 0.0
l: float = 0.0
tempo: float = 0.0
km_l: float = 12.0
vel: float = 0.0

#Inicio
tempo = float(input('Informe o tempo do percurso (em horas): '))
vel = float(input('Informe a velocidade média (em km/h ): '))
dist = tempo * vel
l = dist / km_l
print ('A distância percorrida foi de ', dist, 'km.')
print ('A quantidade de litros gastos foi de', l, 'L')
#Fim