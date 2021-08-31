import os

#Apenas uma função para limpar o console quando é chamado
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

#Função para pausar e reiniciar o programa.
#Def: cria ua função com o nome a seguir
def restart():
    def gotor():
#if: cria uma condição
        pause()
        if pause == "":
            clearConsole()
            restart()
#else: se a primeira condição não aplicar, pula pra essa
        else:
            clearConsole()
            restart()

    def pause():
        input("\nPressione ENTER para continuar...")

    import math as mt
    
#input: abre uma caixa de diálogo para pegar os valores digitados pelo usuário
    x1 = input("Digite o x1: ")
    x2 = input("Digite o x2: ")
    y1 = input("Digite o y1: ")
    y2 = input("Digite o y2: ")

#try: tenta executar o código, se encontrar o erro ValueError, executa o comando que se encontra no except
    try:
        float(x1), float(x2), float(y1), float(y2)
    except ValueError:
        print("Valores não identificados, tente novamente.")
        gotor()

#calc, resp: variáves
#mt.sqrt: importei a função no início do código, facilita a raiz
    calc = mt.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    resp = round(calc, 4)
    print("\nA resposta é: ", resp)
    gotor()

restart()
