import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def restart():
    def gotor():
        pause()
        if pause == "":
            clearConsole()
            restart()
        else:
            clearConsole()
            restart()

    def pause():
        input("\nPressione ENTER para continuar...")

    import math as mt

    x1 = input("Digite o x1: ")
    x2 = input("Digite o x2: ")
    y1 = input("Digite o y1: ")
    y2 = input("Digite o y2: ")

    try:
        float(x1), float(x2), float(y1), float(y2)
    except ValueError:
        print("Valores não identificados, tente novamente.")
        gotor()
        
    calc = mt.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    resp = round(calc, 4)
    print("\nA resposta é: ", resp)
    gotor()

restart()
