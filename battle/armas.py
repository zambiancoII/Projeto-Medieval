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