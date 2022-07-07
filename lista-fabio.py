# forma de importar todas as funçoes de um arquivo
from teste import *
# questão 1
def q1():
    #recebendo os dados
    speed_ms = float(input('Velocidade em m/s: '))

    # processando os dados
    speed_km = speed_ms * 3.6

    # exibindo os dados
    print(f'em km/h: {speed_km}')
# q1()

# questão 2
def q2():
    hr = int(input('horas: '))
    minutos = int(input('minutos: '))
    minutos += hr * 60 

    print(f'em minutos: {minutos}')

# q2()

# questão 3
def q3():
    minutos = int(input('minutos: '))
    horas = minutos // 60
    minutos = minutos % 60

    if horas > 1: print(f'{horas} horas: {minutos} minutos')
    else: print(f'{horas} hora: {minutos} minutos')

#q3()

def q4():
    valor = float(input('valor em dólares: '))
    cotacao_dolar = float(input('cotação atual do dólar: '))
    valor *= cotacao_dolar

    # formatar para duas casas decimais em python
    print(f'valor em R$: {valor:.2f}')

#q4()

def q5():
    numero = int(input('numero de 3 digítos: '))
    c = numero // 100
    d = (numero % 100) // 10
    u = numero % 10
    soma = c + d + u

    print(f'soma dos elementos do número {c} + {d} + {u} = {soma} ')
#q5()

def q6():
    speed_km = float(input('velocidade em km/h: '))
    
    speed_ms = speed_km // 3.6

    print(f'velocidade em m/s: {speed_ms}')
#q6()

def q7():
    a = int(input('primeiro número: '))
    b = int(input('segundo número: '))
    c = int(input('terceiro número: '))

    soma = a + b
    diferenca = b - c

    print(f'\ta soma {a} + {b} = {soma}\n\ta diferença {b} - {c} = {diferenca}')

#q7()

def q8():
    a = int(input('primeiro número: '))
    b = int(input('segundo número: '))

    soma = a + b
    subtracao = a - b

    if soma == 0 or subtracao == 0:
        print('Resultado: divisão impossível')

    else:
        divisao = soma / subtracao
        if isInt(divisao):
            print(f'divisão da soma: {a} + {b} = {soma} pela subtração: {a} - {b} = {subtracao}\n=> resultado da divisão = {int(divisao)}')
        else:
            print(f'divisão da soma: {a} + {b} = {soma} pela subtração: {a} - {b} = {subtracao}\n=> resultado da divisão = {divisao:.1f}')

#q8()

def q9():
    a = int(input('primeiro número: '))
    b = int(input('segundo número: '))

    print(f'números na ordem inversa: {b} | {a}')
#q9()

def q10():
    a = int(input('primeiro número: '))
    b = int(input('segundo número: '))

    quociente = a / b
    resto = a % b

    if isInt(quociente):
        print(f'o quociente da divisão: {a} / {b} = {int(quociente)}\nresto da divisão = {resto}')
    else:
        print(f'o quociente da divisão: {a} / {b} = {quociente:.1f}\nresto da divisão = {resto}')

#q10()

def q11():
    a = int(input('número de três digítos: '))
    numero_inverso(a)

#q11()

def q12():
    salario_inicial = float(input('sálario atual R$: '))

    salario_pos_aumento = reajuste25PorCento(salario_inicial)

    print(f'salário após o reajuste de 25% = R$ {salario_pos_aumento:.2f}')

#q12()

def q13():
    valor = float(input('valor em R$: '))

    setenta_por_cento = setentaPorCento(valor)

    print(f'70% desse valor = R${setenta_por_cento:.2f}')
#q13()

def q14():
    a = float(input('primeira nota: '))
    peso_a = int(input('peso da primeira nota: '))
    b = float(input('segunda nota: '))
    peso_b = int(input('peso da segunda nota: '))
    c = float(input('terceira nota: '))
    peso_c = int(input('peso da terceira nota: '))

    media = media_ponderada_tres_notas(a, peso_a, b, peso_b, c, peso_c)

    if media >= 7:
        print(f'Resultado :aprovado!\nmedia = {media:.1f}')
    else:
        print(f'Resultado: reprovado!\nmedia = {media:.1f}')

#q14() 

def q15():
    base = float(input('base: '))
    altura = float(input('altura: '))
    area = area_triangulo(base, altura)

    if isInt(area):
        print(f'área = {int(area)}')

    else:
          print(f'área = {area}')  

#q15()

def q16():
    lado = float(input('lado: '))

    area = quadrado(lado)

    if isInt(area):
        print(f'área = {int(area)}')

    else:
          print(f'área = {area}') 

#q16()


