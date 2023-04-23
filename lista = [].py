lista_vazia = []
print('''
    1. adicionar o item a lista
    2. apagar o item da lista
    3. listar todos os item na lista
''')

entrada_principal = input("digite um numero corresponde a opçao acima:")

def adicionar():

    while True:
        entrada_temporaria = (input("digite algo que quer adicionar: ").upper())
        lista_vazia.append(entrada_temporaria)
        print(lista_vazia)
        if entrada_temporaria == 'SAIR':
             lista_vazia.remove('SAIR')
             break


if entrada_principal == '1':
    adicionar()

#while True:
    #entrada_usu = str(input("digite algo: ").upper() )
    #lista_vazia.append(entrada_usu)
    #if entrada_usu == "SAIR":
        #lista_vazia.remove ("SAIR") 
        #break
 
    #print(f""" NO MOMENTO SUA LISTA TEM,{lista_vazia}  """)
 

#while True:
    #print("")
    #entrada_remover = str(input("digite o que voçe quer remover:  ") .upper())
    #if entrada_remover == 'SAIR':

      #break
    #try:
        #lista_vazia.remove(entrada_remover)
        #print(lista_vazia)
    # except:
        #print(f'''sua {entrada_remover} nao tem na sua {lista_vazia}''')    
    
   
      
    