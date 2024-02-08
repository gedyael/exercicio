#Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1,
#o código de uma peça 2, o número de peças 2 e o valor 
#unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.
entrada1 = [input().split(' ')]

codigo1 = int(entrada1[0][0])
peca1 = int(entrada1[0][1])
valor1 = float(entrada1[0][2])

multiplicacao = (valor1 * peca1)

entrada2 = [input().split(" ")]

codigo2 = int(entrada2[0][0])
peca2 = int(entrada2[0][1])
valor2 = float(entrada2[0][2])

multiplicacao1 = (valor2 * peca2)

resultado = (multiplicacao + multiplicacao1)

print("VALOR A PAGAR: R$ ""%.2f"%resultado)