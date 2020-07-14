import random
import time
import os

nombre= input("Hola! Como te llamas? ")
print(nombre," es hora de jugar al ahorcado")

jugar= input("jugar? si? no? ")


time.sleep(0.5)
palabra=["murcielago", "amanecer", "mermelada", "lancha", "kiosko", "hamburguesa"]
resultado=" "
vidas=5

palabra = list(random.choice(palabra))



while vidas > 0:
    if jugar=="si":
        print(" a jugar!")
        time.sleep(1)
    else:
        print("FIN.")
        break


    fallas=0
    for letra in palabra:
        if letra in resultado:
            print(letra,end="")
        else:
            print("_ ",end="")
            fallas+=1

    if fallas==0:
        input()
        print("")
        print(" FELICIDADES!, ganaste!!")
        input()
        break

    elijeletra=input(" introduce una letra: ")
    resultado+=elijeletra

    if elijeletra not in palabra:
        vidas-=1
        print(" Error!")
        print(" tu tienes ",+vidas," vidas")
    if vidas== 0:
        print(" Perdiste! palabra= ") 
        print(list(random.choice(palabra)))
        print("Gracias por participar.")
   

    #os.system ("cls")
