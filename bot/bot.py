import os
from funcoes_bot import *
def bot():
    print('olá, sou o Bot.')

    ask_name = input('\nE você, como se chama?\nsua resposta: ')

    print(f'\n\t --- seja bem-vindo, {ask_name} ---')

    ask_menu = int(input('\ndeseja visualizar o menu? (1-sim ou 2-não)\nsua resposta: '))

    if ask_menu == 1:
        menu()

        opcao = int(input('\nsua opção: '))

        while opcao != 0:
            if opcao == 1:
                menu_operacoes()
                ask = int(input('\nselecione a operação: '))

                operacoes(ask)

            enterToContinue()
            print("\n" * os.get_terminal_size().lines)
            menu()
            opcao = int(input('\nsua opção: '))

            if opcao == 2:
                calcularIdade()

            enterToContinue()
            print("\n" * os.get_terminal_size().lines)
            menu()
            opcao = int(input('\nsua opção: '))     

    else:
        print(f'\nBot diz : Blz, vá com Jesus, {ask_name}.\nE a paz de Deus, que excede todo o entendimento, guardará os vossos corações e\nos vossos pensamentos em Cristo Jesus. Filipenses 4:7')

def menu():
    menu = '\nselecione uma tarefa para o Bot\n'
    menu += '\nmenu de opções do Bot\n'
    menu += '\n[1] -> operações com dois números: somar, subtrair, dividir ou multiplicar'
    menu += '\n[2] -> adivinhar sua idade'
    menu += '\n[3] -> dizer a quantidade de dias que faltam para o fim do ano'
    menu += '\n[4] -> indicar uma música'
    menu += '\n[0] -> sair'
    print(menu)

def operacoes(awnser):
    n1 = float(input('primeiro número: '))
    n2 = float(input('segundo número: '))

    if awnser == 1:
        resultado = n1 + n2
    elif awnser == 2:
        resultado = n1 - n2
    elif awnser == 3:
        resultado = n1 / n2
    else:
        resultado = n1 * n2    


    if ehInt(resultado):
        print(f'resultado = {int(resultado)}')
    else:
        print(f'resultado = {resultado}')


def menu_operacoes():
    print('\n menu de operações')
    operacoes =  '[1] somar'
    operacoes += '\n[2] subtrair'
    operacoes += '\n[3] dividir'
    operacoes += '\n[4] multiplicar'
    print(operacoes)

def enterToContinue():
    enter = input('\naperte enter para continuar...')
    print("\n" * os.get_terminal_size().lines)

bot()
