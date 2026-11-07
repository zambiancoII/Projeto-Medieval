def battle():
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