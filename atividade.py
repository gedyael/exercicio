cov = (input(" oi bom dia tudo bem? "))
nome = (input(" como se chama? "))
id = int(input("por gentileza digite seu id: "))
hora = float(input(" otimo agora me diga quantas horas trabalhadas: "))
custo = float(input("poderia me dizer seu custo? "))

resultado = (hora*custo)
print("obrigado", nome , "o seu salario desse mes e de: " "R$", "%.2f" % resultado)
 
input(exit)     
