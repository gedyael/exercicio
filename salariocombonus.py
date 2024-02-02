nome = str(input())
salario = float(input())
valor_vendas = float(input())

desconto = (valor_vendas * 15 )/100

resultado = desconto + salario

print("TOTAL = R$","%.2f"%resultado)
