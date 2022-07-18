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

def q2():
    hr = int(input('horas: '))
    minutos = int(input('minutos: '))
    minutos += hr * 60 

    print(f'em minutos: {minutos}')

# q2()

def q3():
    minutos = int(input('minutos: '))
    horas = minutos // 60
    minutos = minutos % 60

    # if em uma linha
    if horas > 1: print(f'{horas} horas: {minutos} minutos')
    else: print(f'{horas} hora: {minutos} minutos')

#q3()

def q4():
    valor = float(input('valor em dólares: '))
    cotacao_dolar = float(input('cotação atual do dólar: '))
    valor *= cotacao_dolar

    # formatar valor para duas casas decimais em python
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
        if ehInt(divisao):
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

    if ehInt(quociente):
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

    exibirArea(area)  

#q15()

def q16():
    lado = float(input('lado: '))

    area = quadrado(lado)

    exibirArea(area)

#q16()

def q17():
    base = float(input('base: '))
    altura = float(input('altura: '))

    area = areaRetangulo(base, altura)

    exibirArea(area) 

#q17()

def q18():
    raio = float(input('raio: '))

    c = calcularComprimentoRaio(raio)

    exibirArea(c)

#q18()

def q19():
    raio = float(input('raio: '))

    volume = calcularVolumeEsfera(raio)

    ask = int(input('deseja visualizar o resultado arredondado ? (1-sim ou 2-nao)\nresposta: '))

    if ask == 1:
        print(f'volume = {volume:.2f}')
    else:
        print(f'volume = {volume}') 

#q19()

def q20():
    tempC = float(input('temperatura em graus celsius: '))

    tempF = converterFahrenheit(tempC)

    exibirTemperatura(tempF)

#q20()

def q21():
    tempF = float(input('temperatura em graus fahrenheit: '))

    tempC = converterCelsius(tempF)

    exibirTemperatura(tempC)

#q21()

def q22():
    km = float(input('kilometros: '))

    m = kmOuKg(km)

    if ehInt(m):
        print(f'==> = {int(m)} metros')
    else:
        print(f'==> = {m} metros')

#q22()

def q23():
    kg = float(input('kilogramas: '))

    g = kmOuKg(kg)

    if ehInt(g):
        print(f'==> = {int(g)} gramas')
    else:
        print(f'==> = {g} gramas')

#q23()


def q24():
    m = float(input('metros: '))

    cm = mParaCm(m)

    if ehInt(cm):
        print(f'==> = {int(cm)} centímetros')
    else:
        print(f'==> = {cm} centímetros')

#q24()

def q25():

    while True:
        m = float(input('metros: '))

        if ehInt(m):
            break

    [km, m_resto] = m_para_km_e_m(m)

    print(f'== {int(km)} kilometro(s) e {int(m_resto)} metro(s)')

#q25()

def q26():
    while True:
        dias = float(input('dias: '))

        if ehInt(dias):
            break
        
    [semanas, resto_dias] = dias_para_semanas_e_dias(dias)

    print(f'== {int(semanas)} semana(s) e {int(resto_dias)} dia(s)')

#q26()

def q27():
    count = 0
    while True:
        segundos = float(input('segundos: '))
        
        count += 1
        if ehInt(segundos):
            print(f'quantidade de tentativas: {count}')
            break
        
    [horas, minutos, segundos_resto] = segundos_para_hr_min_segs(segundos)
    
    print(f'== {int(horas)} hora(s), {int(minutos)} minuto(s) e {int(segundos_resto)} segundo(s)')
        
#q27()

def q28():
    while True:
        horas = float(input('horas: '))
        
        if ehInt(horas):
            break
        
    [semanas, dias, horas_resto] = horas_para_semanas_dias_horas(horas)
        
    print(f'== {int(semanas)} semana(s), {int(dias)} dia(s) e {int(horas_resto)} hora(s) ')

#q28()

def q29():
    while True:
        
        meses = float(input('meses: '))
        
        if ehInt(meses):
            break
        
    [anos, resto_meses] = meses_para_anos_e_meses(meses)
    
    print(f'== {int(anos)} ano(s) e {int(resto_meses)} mes(es)')
    
#q29()

def q30():
    while True:
        minutos = float(input('minutos: '))
        
        if ehInt(minutos):
            break
    
    [dias, horas, resto_minutos] = horas_para_dias_horas_e_minutos(minutos)  
        
    
    print(f'{int(dias)} dia(s), {int(horas)} hora(s) e {int(resto_minutos)} minuto()')
    
#q30()

def q31():
        
    binario = int(input("número (binário) de 4 digítos: "))

    decimal = converterBinarioParaDecimal(binario)

    print(f'na base decimal = {decimal}')
    
    
q31()

    
    