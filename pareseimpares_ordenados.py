#CRIE UMA ENTRADA QUE CONTEM UM UNICO NUMERO INTEIRO INTEIRO POSITIVO
escolha = int(input('Quantos numeros deseja inserir: '))
#CRIAÇAO DE LISTA PARES E IMPARES
lista_pares = []
lista_impares = [] 
# LAÇO CRIADOR PRA INFORMAR OS NUMEROS INSERIDOS E ACRESCENTALOS NA LISTA
for i in range(escolha):
    n = int(input('Digite o numero: '))
    if n % 2 == 0:
        lista_pares.append(n)   
    else:
        lista_impares.append(n) 
#ORDENANDO LISTA
lista_pares.sort() 
#REVERTENDO LISTA
lista_impares.reverse()  
#PRINTANDO LISTA
print(lista_pares)
print(lista_impares)
        