# entrada = (input('digite o numero inteiro para fazer a multiplicaçao: '))

# multiplicaçao = entrada.isnumeric()

# if multiplicaçao == True:
#     n1 = int(input('digite o primeiro numero: '))
#     n2 = int(input('digite o primeiro numero: '))
#     soma_multiplicaçao = n1 * n2
#     if soma_multiplicaçao :
#         print(f'''sua soma foi de{soma_multiplicaçao},e seu o que voce digitou e {multiplicaçao}''')  
#     else:
#         print('o que foi digitado nao foi inteiro')    
import time

class Calcular():
    def __init__(self,a,b):
        self.numero1 = a
        self.numero2 = b
    def somar(self):
        return self.numero1 + self.numero2
    def multiplicar(self):
        return self.numero1 * self.numero2
    def Subtrair(self):
        return self.numero1 - self.numero2
    def dividir(self):
        return self.numero1 / self.numero2

try:
    numero1 = int(input('informe um Numero: '))
    numero2 =int(input('informe outro Numero: '))   
  

    print('Calculando os Resultado....')

    time.sleep(2)

    Resultado = Calcular(numero1,numero2)

    def Mostrar_Resul():
        print(f''''O Resultado da sua Multiplicaçao é: {Resultado.multiplicar()}
        ***************************
        'O Resultado da sua Soma é: {Resultado.somar()}
        *******************************
        'O Resultado da sua Subtração é: {Resultado.Subtrair()}
        *******************************
        'O Resultado da sua Divisão é: {Resultado.dividir()}''')
    Mostrar_Resul()        
except:
    print('erro...')
        
