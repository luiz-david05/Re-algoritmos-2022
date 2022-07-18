import os

def calcularIdade():
    data_nascimento = input('data de nascimento no formato (dd/mm/aaaa): ').split('/')
    data_atual = input('data atual: ').split('/')
    ints = []

    # converter um array/lista para números inteiros --
    for elemento in data_nascimento:
        ints.append(int(elemento))

    [dia_nasc, mes_nasc, ano_nasc] = ints


    inteiros = []
    
    for elemento in data_atual:
        inteiros.append(int(elemento))

    [dia_atual, mes_atual, ano_atual] = inteiros

    idade = ano_atual - ano_nasc
    

    if dia_nasc > dia_atual or mes_nasc > mes_atual:
        idade -= 1

    print(f'\nsua idade é {idade} anos.')

def ehInt(n):
    return n % 1 == 0

def enterToContinue():
    enter = input('\naperte enter para continuar...')
    print("\n" * os.get_terminal_size().lines)