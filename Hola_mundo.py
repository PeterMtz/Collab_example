# Pedro Martinez
print('Hola mundo Pedro Mtz')

# Pris Cvts
print('Hola mundo Pris Cvts')

# JP ECH
print('Hola mundo Juan Pablo Ech')

# Ivanna Camerota
print('Hola mundo Ivanna')

#Mariana
print('Hola mundo Salo')

#Remi
print('Hola mundo Remi')

print('Hola mundo est')

#MAX
print('Hola mundo max aaaa dejame editar')

# Diego Canales 
print('Hola mundo Diego')

import random
import sys
import time

def ruleta_rusa_segura(camaras=6):
    print("🎲 Ruleta rusa (segura) — nada se borra, solo se termina el programa si pierdes.")
    bala = random.randint(1, camaras)
    for i in range(1, camaras + 1):
        input(f"Cámara {i}. Presiona Enter para gatillar… ")
        if i == bala:
            print("💥 ¡BANG! Perdiste (de mentiritas). Cerrando…")
            time.sleep(1.2)
            sys.exit(0)
        else:
            print("click… te salvaste.")

if __name__ == "__main__":
    while True:
        ruleta_rusa_segura()
        otra = input("¿Juegas otra vez? [s/N] ").strip().lower()
        if otra != "s":
            print("👋 Fin del juego. Nada fue dañado.")
            break

stop playing 

# David Gutierrez
print('Divad odnum aloH')



