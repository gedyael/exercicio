# Criar um programa de quanto vc ganha por horas, e horas trabalhadas no mês.
# calcule e mostre o salario bruto
# Descontado:
# If 11%
# Inss 8
# sindicato 5%
for i in range(3):
    Nome_Funcionario = str(input('Qual seu nome: ').upper())
    Identificacao = int(input('Qual seu numero de identificação: '))
    Horas_Trabalhadas = int(input('Quantas horas trabalhadas: '))
    break

Ganho_Por_Horas = 5.00 
Imposto_de_renda = 11/100 # 0,11%
Inss = 8/100 # 0,08%
Sindicato = 5/100 #0,05%
Salario_Bruto = Horas_Trabalhadas * Ganho_Por_Horas
Salario_Liquido = Salario_Bruto - (Salario_Bruto * Imposto_de_renda) - (Salario_Bruto * Inss)  - (Salario_Bruto * Sindicato)
#                    500,00     - (          55,00 = 445,00        ) - (     40,00 = 405    )  - (       25,00 = 380,00    )
#  Calculos acima baseados no valor de 100 horas trabalhadas.

print(f'''
    *************************
    FUNCIONARIO DE ID: {Identificacao}
    NOME FUNCIONÁRIO: {Nome_Funcionario}
    HORAS TRABALHADAS: {Horas_Trabalhadas}
    SALARIO BRUTO DE:R$ {'%.2f'%Salario_Bruto}
    SALARIO LIQUIDO:R$ {'%.2f'%Salario_Liquido}
    *************************
''')