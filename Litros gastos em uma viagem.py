# calcular e mostrar a quantidade de litros gasto em uma viagem sabendo que o automovel faz 12 km/L
# para efetuar o calculo, deve se fornecer o tempo gasto na viagem (em horas)
# e a velocidade media durante a mesma (em Km/h). 
# em seguida calcular quantos seriam seriam necessario
# obs: mostre o valor com 3 casas decimais. 
# obs: o arquivo de entrada deve conter 2 inteiro, o primeiro e o tempo gasto na viagem (Em Horas ) eo
# segundo e a velocidade media durante a mesma (em Km/L)
print("----------------------------------------------- ")
print("          LITROS GASTO EM UMA VIAGEM            ")
print("------------------------------------------------")
tempo_gasto = int(input("informe quantas horas sera a sua viagem? "))
velocidade_media = int(input("informe qual sera sua velocidade media? "))
automovel = 12
resultado = (tempo_gasto*velocidade_media)/automovel

print("a quantidade de litros gastos sera de : ", "%.3f"% resultado,"litros")