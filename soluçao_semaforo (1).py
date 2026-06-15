# Bibliotecas que vamos usar
import time
import random

# Fica rodando para sempre
while True:

    # Sorteia quantos carros tem em cada via
    vias = [
        random.randint(0, 30),
        random.randint(0, 30)
    ]

    # Mostra a quantidade de carros
    print("\nCarros na Via 1:", vias[0])
    print("Carros na Via 2:", vias[1])

    # Se a Via 1 tiver mais carros
    if vias[0] > vias[1]:

        # Calcula o tempo do sinal verde
        tempo1 = vias[0] // 2 + 5
        tempo2 = vias[1] // 2 + 5

        # Via 1 abre primeiro
        print("\n🚦 Via 1 está VERDE por", tempo1, "segundos")
        time.sleep(tempo1)

        # Depois abre a Via 2
        print("🚦 Via 2 está VERDE por", tempo2, "segundos")
        time.sleep(tempo2)

    else:

        # Faz a mesma conta para os tempos
        tempo2 = vias[1] // 2 + 5
        tempo1 = vias[0] // 2 + 5

        # Via 2 abre primeiro
        print("\n🚦 Via 2 está VERDE por", tempo2, "segundos")
        time.sleep(tempo2)

        # Depois abre a Via 1
        print("🚦 Via 1 está VERDE por", tempo1, "segundos")
        time.sleep(tempo1)

    # Começa tudo de novo
    print("\n--- reiniciando ---")
