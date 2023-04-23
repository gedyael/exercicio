
#criando uma variável lista vazia

numeros = [1,2,6,6,5,48,6,3,0,6]

# Criando uma lista com os numeros de 1 a 10

lista = ['a',"e","i","o","u", 1, "1"]

# Criando uma lista mista

lista = [1.9,True,"a","b",2,3,4,5,"c",6,7,"d",8,9,10,["otni", "joaquina"]]

# Criando uma variavel exemplo
variavelExemplo = ["123"]

# Adicionando em uma lista
lista.append(variavelExemplo)

#printando a lista
#print(lista)

# Printando um objeto pela possição na lista
#print(lista[15])

# Verificando o tamanho de uma lista
#print(len(lista))

# Removendo em uma lista
#lista.remove(lista[0])

#printando a lista
#print(lista)

variavelExemplo = 23

# Adicionando em uma possição específica da lista
lista.insert(0,variavelExemplo)

#printando a lista
#print(lista)

# retorna o numeto de vezes que o parametro aparece na lista
#print(numeros.count(6))

quant =  int(input("Digite a quantida de numeros que você quer somar: "))
list = []

#for i in range(0,quant):
#    x = int(input("Digite um número: "))
#    list.append(x)

while len(list) < quant:
   x = int(input("Digite um número: "))
   list.append(x)

#soma = list[0] + list[1]

while len(list) != 0:
    if x in list:
        print(list[0])
        list.remove(list[0])


print("O que sobra na lista é:", list)