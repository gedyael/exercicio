n = int(input('informe um numero: '))
cont = 0
while True:
    if n % 2 !=0:
        print(n)
        cont+=1
    n+=1
    if cont==6:
        break    
    