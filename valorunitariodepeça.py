#Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1,
#o código de uma peça 2, o número de peças 2 e o valor 
#unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

codigo_1 = int(input())
peca_1 = float(input())
valor_uni_1 = float(input())

codigo_2 = int(input())
peca_2 = float(input())
valor_uni_2 = float(input())

soma = (valor_uni_1 * peca_1) 
soma2 = (valor_uni_2 * peca_2)

resultado = soma + soma2

print(resultado)