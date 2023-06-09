class calculadora:
    def __init__(self,numero1,numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def multiplicaçao(self):
        print('sua multiplicaçao e de:',self.numero1 * self.numero2)

    def divisao(self):
        print('Sua Divisao e de:',self.numero1 / self.numero2)  

    def soma(self):
        print('Sua Soma e de:',self.numero1 + self.numero2)

    def subtraçao(self):
        print('Sua Subtração e de:',self.numero1 - self.numero2)

    def divisao_inteira(self):
        print('Sua Divisão Inteira e de:',self.numero1 // self.numero2)

    def potenciaçao(self):
        print('Sua Potencia e de:',self.numero1 ^ self.numero2)  

    def expotençiação(self):
        print('Sua Expotençiação e de:',self.numero1 ** self.numero2) 


Resultado = calculadora(10,5)
Resultado.multiplicaçao()
Resultado.divisao()
Resultado.soma()
Resultado.subtraçao()
Resultado.divisao_inteira()
Resultado.potenciaçao()
Resultado.expotençiação()