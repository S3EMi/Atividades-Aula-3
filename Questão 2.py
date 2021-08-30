import os, math

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def restart():
    def gotor():
        if pause() == "":
            clearConsole()
            restart()
        else:
            clearConsole()
            restart()

    def pause():
        input("\nPressione ENTER para continuar...")
    
    kmh = input("Digite a velocidade média da viagem: ")
    h = input("Digite o tempo da viagem (em horas): ")
    
    try:
        float(h), float(kmh)
    except ValueError:
        print("Valores não identificados, tente novamente.")
        gotor()
    except Exception:
        print("Aconteceu um erro, tente novamente.")

    cal = (float(kmh)*float(h))
    litrosn = round(cal/12, 3)
    print("\nSerá necessário ", litrosn, " Litros.")
    gotor()

restart()
