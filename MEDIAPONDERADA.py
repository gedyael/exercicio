n1 = float(input("Digite a nota A: "))
n2= float(input("Digite a nota B:"))

peso_a = 3.5
peso_b = 7.5

#Calcula a média
media = (n1 * peso_a + n2* peso_b)/(peso_a + peso_b)

#Exibe a média 
print("A média ponderada do aluno é:",'%.5f'% media)
              