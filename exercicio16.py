#Declarar
valor_p_hora: float = 0.0
quantidade_horas: float = 0.0
perc_desconto: float = 0.0
num_dependentes: float = 0.0
sal_liq: float = 0.0
desc_total: float = 0.0
sal_bruto: float = 0.0
sal_receber: float = 0.0

#Inicio
quantidade_horas = float(input('Informe a quantidade de horas trabalhadas: '))
valor_p_hora = float(input('Informe o valor recebido por horas trabalhadas: '))
perc_desconto = float(input('Informe o percentual de desconto: '))
num_dependentes = float(input('Informe o número de dependentes: '))
sal_bruto = valor_p_hora * quantidade_horas
desc_total = sal_bruto * (perc_desconto / 100)
sal_liq = sal_bruto - desc_total
sal_receber = sal_liq + (num_dependentes * 100)
print ('O valor sobre os dependentes é de: ', (num_dependentes * 100))
print ('O desconto total do seu salário (sem contar dependentes) é de: ', desc_total)
print ('O salário bruto é: ', sal_bruto)
print ('O salário a receber é de: ', sal_receber)
#Fim
