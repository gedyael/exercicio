#Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
#a) a área do triângulo retângulo que tem A por base e C por altura.
#b) a área do círculo de raio C. (pi = 3.14159)
#c) a área do trapézio que tem A e B por bases e C por altura.
#d) a área do quadrado que tem lado B.
#e) a área do retângulo que tem lados A e B.
#Entrada
#O arquivo de entrada contém três valores com um dígito após o ponto decimal.

#Saída
#O arquivo de saída deverá conter 5 linhas de dados. Cada linha corresponde a 
#uma das áreas descritas acima, sempre com mensagem correspondente e um espaço entre os dois pontos e o valor.
#O valor calculado deve ser apresentado com 3 dígitos após o ponto decimal.


valores = [(input().split(" "))]
A = float(valores[0][0])
B = float(valores[0][1])
C = float(valores[0][2])

Pi = 3.14159
calculo_area_do_trianguloretangulo = (A * C) /2
calculo_do_circulo= (Pi * C**2)
calculo_do_trapezio = (A + B)*C /2
calculo_do_quadrado = B**2
calculo_do_retangulo = A * B

print("TRIÂNGULO:", "%.3f"%calculo_area_do_trianguloretangulo)
print("CÍRCULO:", "%.3f"%calculo_do_circulo)
print("TRAPÉZIO:", "%.3f"%calculo_do_trapezio)
print("QUADRADO:", "%.3f"%calculo_do_quadrado)
print("RETÂNGULO:", "%.3F"%calculo_do_retangulo)