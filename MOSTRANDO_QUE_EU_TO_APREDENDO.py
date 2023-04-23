lista = []

while True:
    entrada_1 = str(input('me informe um produto: ').upper())
    lista.append(entrada_1)
    if entrada_1 == 'SAIR':
        lista.remove('SAIR')
        break
print(lista)
while True:
    entrada_2 = str(input(' informe qual produto quer remover: ').upper())
    if entrada_2 == 'SAIR':
     break
    try:
        lista.remove(entrada_2)
        print(lista)
    except:
         print(f'na sua lista nao tem: {entrada_2} ')
    


print(lista)