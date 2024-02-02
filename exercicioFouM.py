# faça um programa que diga F= FEMININO E M = MASCULINO E OUTRA LETRA QUE NAO FOR ESSA QUE SEJA INVALIDA

valor = str(input('ME INFORME UMA LETRA: ').upper())

if  valor == 'M':
    print('MASCULINO')
elif valor == 'F':
    print('FEMININO')
else:
    print('INVALIDO')        