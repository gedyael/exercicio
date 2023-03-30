#leia 3 numeros e mostre o maior dele
num1 = int(input("digite um numero: "))
num2 = int(input("digite segundo numero: "))
num3 = int(input("digite outro numero: "))
um = num1
dois = num2
tres = num3
if (um > dois and tres):
    print(num1, "e maior")        
elif (dois > tres and um):
    print(num2, "e maior ") 
elif (tres > dois and um):
    print(num3 ,"e maior ")          
else:
    print("=====================")
    print("   opçao invalida    ")
    print("======================")
   

    

                