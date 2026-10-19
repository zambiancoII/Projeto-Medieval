import random,os,time

def clear():
    os.system('cls')
###Escolher a arma do jogador, onde terá o dano, defesas, criticos###
def weapon(arma):
    while True:
        arma=input("qual armar vc escolhe?").lower()
        if arma == "arco":
            weapon=5
            
            break
        elif arma == "espada longa":
            weapon=8
            
            break
        elif arma == "espada curta e escudo":
            weapon=6
            
            break
        elif arma == "machado":
            weapon=12
            break
        else:
            print("favor selecione uma arma valida!!")
    
    print(f"Voce escolheu {arma} como arma")
    return weapon

###Sistema de batalha###
def battle(arma):
    hp_char=50
    hp_enemy=50
    while hp_enemy>0 and hp_char>0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"HP Rafael {hp_char}")
        print(f"HP Enemigo{hp_enemy}")
        atk_char=arma
        atk_enemy=random.randint(1,10)
        atk=random.randint(1,atk_char)
        print("voce ataca e...")
        cont=input()
        if atk <2:
            print("erra o ataque")
            cont=input()
            
        else:
            print(f"voce inflinge {atk} de dano")
            hp_enemy-=atk
            print(f"o inimigo esta com {hp_enemy} de vida")
            cont=input()
        print("-----------------")
        
        if hp_enemy<=0:
            print("Seu adversario acaba Falecendo, voce venceu!!!")
        else:
            print("Vez do adversario")
            print("Ele ataca e...")
            cont=input()
            
            if hp_enemy >0 and atk_enemy < 2:
                print("erra o ataque")
                cont=input()
            elif hp_enemy>0 and atk_enemy>=2:
                print(f"acerta e inflinge {atk_enemy} de dano")
                hp_char-=atk_enemy
                cont=input()
                if hp_char<1:
                    print("Voce morreu, tente novamente!!")
                    cont=input()
                else:
                    print("-----------------")
                    cont=input()
nome=input("qual o nome do(a) nobre jogador(a): ")
print("selecione a sua arma:")
print("arco, espada longa, espada curta e escudo, machado")
arma=0
arma=weapon(arma)
time.sleep(5)
clear()
###Codigo Principal### 
print(f"   Existia uma lenda na vila de Oak Heaven")
time.sleep(3)
print(f"   A vila onde {nome} cresceu, seus dias eram passados na forja de seu pai ou caçando nas matas próximas para garantir o jantar.")
time.sleep(5)
clear()
print(f"   Você era conhecido(a) por ser jovem de 'olhos atentos' — aquela que percebia a mudança do vento antes de uma tempestade ou o rastro de uma fera que ninguém mais via.")
time.sleep(10)
clear()
print(f"   Foi essa intuição que chamou a atenção de Alaric anos atrás, quando ele passou pela vila e viu em você uma centelha de coragem que nem você sabia que tinha.")
time.sleep(10)
clear()
print(f"   Na manhã em que tudo mudou, o sol nasceu estranhamente alaranjado.")
print(f"   {nome} estava no pátio do monastério da Ordem, praticando seus movimentos básicos com uma espada de treino feita de madeira.")
time.sleep(15)
print(f"   Quando ao ser derrubado pelo seu parceiro de treino percebe as nuvens tomando um padrão, ate então, nunca visto")
time.sleep(10)
clear()
print(f"   {nome} se levanta rapidamente e se dirige para as muralhas da vila.")
time.sleep(5)
print(f"   Enquanto percorre a vila, percebe que os animais estão inquietos, galinhas tentando escapar das gaiolas, vacas mugindo, cavalos tentando se soltar dos palanques, aves voando para a outra direção, {nome} estava percebendo que não é coincidencia isso tudo")
time.sleep(15)
print(f"   Chegando na muralha, {nome} observa os guardas ficando em prontidão, como se aguardassem um ataque")
print(f"   {nome} pergunta: '-O que esta havendo?Por que está esse caos na vila e esse alvoroço na muralha?'")
time.sleep(15)
clear()
print(f"Antes mesmo de ter algum tipo de resposta, acontece uma grande explosão e um brilho chama a atenção de todos!")
time.sleep(10)
clear()
print("            .")
print("         .  ^  .")
print("    '.   < {火} >   .'")
print("         '  v  '")
print("            '")
print("         _ __ _")
print("   (  _ _  _ _  _  )")
time.sleep(0.2)
clear()
print("             .")
print("             '     '")
print("      .      ^      .")
print("     :    < { } >    :")
print(" '--.  < { {火} } >  .--'")
print("     :    < { } >    :")
print("      '      v      '")
print("          .     .")
print("             '")
print("      _ __ ___ __ _")
print("    (  _ _  _ _  _  )")
print("  ((_(  _  _  _  _  )_))")
time.sleep(0.2)
clear()
print("            .")
print("         .  ^  .")
print("    '.   < {火} >   .'")
print("         '  v  '")
print("            '")
print("         _ __ _")
print("   (  _ _  _ _  _  )")
time.sleep(0.2)
clear()
print("             .")
print("             '     '")
print("      .      ^      .")
print("     :    < { } >    :")
print(" '--.  < { {火} } >  .--'")
print("     :    < { } >    :")
print("      '      v      '")
print("          .     .")
print("             '")
print("      _ __ ___ __ _")
print("    (  _ _  _ _  _  )")
print("  ((_(  _  _  _  _  )_))")
time.sleep(0.2)
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
