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

    x1 = float(input("Digite o x1: "))
    x2 = float(input("Digite o x2: "))
    y1 = float(input("Digite o y1: "))
    y2 = float(input("Digite o y2: "))

    calc = mt.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    resp = round(calc, 4)
    print("\nA resposta é: ", resp)
    gotor()

restart()