num1 = int(input("digite um numero: "))
num2 = int(input("digite segundo numero: "))
num3 = int(input("digite outro numero: "))

if (num1 > num2 and num1 > num3):
    print(num1, "e maior")        
elif (num2 > num3 and num2 > num1):
    print(num2, "e maior ") 
elif (num3 > num2 and num3  > num1):
    print(num3 ,"e maior ") 

if (num1 < num2 and num1 < num3):
    print(num1, "e menor")        
elif (num2 < num3 and num2 < num1):
    print(num2, "e menor ") 
elif (num3 < num2 and num3 < num1):
    print(num3 ,"e menor ") 
      
else:
    print("=====================")
    print("   todos sao iguais    ")
    print("======================")
