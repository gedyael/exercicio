vermelho = '\033[31m'
defalt = '\033[m'
verde = '\033[32m'
print(f'''
  {vermelho} 
   ###    ##     ## ######## ########  ####  ######     ###    ##    ##    ###     ######  
  ## ##   ###   ### ##       ##     ##  ##  ##    ##   ## ##   ###   ##   ## ##   ##    ## 
 ##   ##  #### #### ##       ##     ##  ##  ##        ##   ##  ####  ##  ##   ##  ##       
##     ## ## ### ## ######   ########   ##  ##       ##     ## ## ## ## ##     ##  ######  
######### ##     ## ##       ##   ##    ##  ##       ######### ##  #### #########       ## 
##     ## ##     ## ##       ##    ##   ##  ##    ## ##     ## ##   ### ##     ## ##    ## 
##     ## ##     ## ######## ##     ## ####  ######  ##     ## ##    ## ##     ##  ######  {defalt} ''')


vent = int(input("qual e o preço de um ventilador? "))
tv = int(input("qual e o preço de uma televisao? " ))
ce = int(input("qual e o preço desse smartphone? "))
def escolha ():

    if (vent < tv and vent < ce):
        print("=====================================================================")
        print(" voce devera escolher o ventilador por que e o produto mais barato ")
        print("=====================================================================")
    elif ( tv < vent and tv < ce):
        print("=====================================================================")
        print("voce deverar esolher a televisao por que e o produto mais barato")
        print("=====================================================================")  
    elif ( ce < vent and ce < tv):
        print("==================================================================")
        print(" voce devera escolher o smartphone por que o produto e mais barato")
        print("==================================================================") 
    elif ( (vent==tv) and (vent==tv) and (tv==ce) and (tv==vent) and (tv==ce) and (ce==vent) and (ce==tv)):
        print(" aproveita a oferta por que todos os produtos estao na promoçao")   

    else :
        (" voce deverar escolher nenhuma da opçao")         
        #fim
escolha()        