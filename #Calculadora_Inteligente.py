#selecionar qual cor por no print 
blue= '\033[36m'
red = '\033[31m'
close = '\033[m'
#print das operações
print(f'''             {red} OPERACOES{close}
{blue}         1- adicao
         2- multiplicação
         3- subtração
         4- divisão
            {close}''')

# def criado para a soma 
def soma ():
    while True:
        entrada_1 = str((int(input('qual operacões a seguir desejar resolver? '))))  
        N1 = int(input('informe o numero: '))
        N2 = int(input('informe outro numero: '))
        S_ADIÇÃO = N1 + N2
        S_MULTIPICACÃO = N1 * N2
        S_SUBTRAÇÃO = N1 - N2
        S_DIVISÃO = N1 / N2
        if entrada_1 == '1':
            print(f'sua soma foi de {S_ADIÇÃO}')
            entrada_2 = str(input('deseja fazer outra operação? '). upper())

        if entrada_1 == '2':
            print(f'sua soma foi de {S_MULTIPICACÃO}')
            entrada_2 = str(input('deseja fazer outra operação? '). upper())

        if entrada_1 == '3':
            print(f'sua soma foi de {S_SUBTRAÇÃO}')
            entrada_2 = str(input('deseja fazer outra operação? '). upper())

        if entrada_1 == '4':
            print(f'sua soma foi de {S_DIVISÃO}')
            entrada_2 = str(input('deseja fazer outra operação? '). upper())
                        
        if entrada_2 == 'SIM':
            (entrada_1)
        if entrada_2 == 'NAO':
            print('Fechando programa....')
            break    
soma()    
    
       
        

                   
                    