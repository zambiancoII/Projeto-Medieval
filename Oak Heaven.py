import random,os,time

def clear():
    os.system('cls')
nome=input("qual o nome do(a) nobre jogador(a): ")
print("selecione a sua arma:")
print("arco, espada longa, espada curta e escudo, machado")
arma=0
arma=weapon(arma)
time.sleep(5)
clear()
###Codigo Principal### 


clear()
print(f"{nome}olha com espanto, percebendo uma figura saindo do meio da fumaça enegrecida. 'Quem seria?' pensou, de repente se escuta um grito, como se fose um rugido.")
print(f"    Logo atras surgem varias criaturas estranha, onde nunca foram vistas naquelas terras correndo e adentrando a sua vila.")
x=0
match arma:
    case "arco":
        x= "um arco"
    
    case "espada longa":
        x= "uma espada longa"
        
    case "espada curta e escudo":
        x= "uma espada curta e um escudo"
    case "machado":
        x= "um machado"
print(f"    {nome} vira para o lado e vê jogado no chao {x}")
