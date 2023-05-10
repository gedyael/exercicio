entrada = (input('digite o numero inteiro para fazer a multiplicaçao: '))

multiplicaçao = entrada.isnumeric()

if multiplicaçao == True:
    n1 = int(input('digite o primeiro numero: '))
    n2 = int(input('digite o primeiro numero: '))
    soma_multiplicaçao = n1 * n2
    if soma_multiplicaçao :
        print(f'''sua soma foi de{soma_multiplicaçao},e seu o que voce digitou e {multiplicaçao}''')  
    else:
        print('o que foi digitado nao foi inteiro')    