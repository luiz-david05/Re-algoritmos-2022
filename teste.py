# testando import 
def hello() :
    nome = input('digite seu nome: ')
    print(f'\t--- {nome}, tomar no teu cu, rapá!---')

def isInt(numero):
     return numero == round(numero)

def numero_inverso(numero):
    c = numero // 100
    d = (numero % 100) // 10
    u = numero % 10     
    print(f'inverso = {u}{d}{c}')

def reajuste25PorCento(salario):
    aumento = salario * (25 / 100)
    salario += aumento
    return salario

def setentaPorCento(valor):
    return valor * (70 / 100)

def media_ponderada_tres_notas(a,p1, b, p2, c, p3):
    media = ((a * p1) + (b * p2) + (c * p3)) / (p1 + p2 + p3)
    return media

def exibirArea(area):
    if isInt(area):
        print(f'área = {int(area)}')

    else:
        print(f'área = {area}')

def area_triangulo(base, altura):
    return (base * altura) / 2 

def quadrado(n):
    return n * n

def areaRetangulo(base, altura):
    return base * altura

def calcularComprimentoRaio(raio):
    return 2 * 3.14 * raio

def calcularVolumeEsfera(raio):
    return (4 * 3.14 *  raio ** 3) / 3

def converterFahrenheit(temperatura):
    return (9 * temperatura + 160) / 5

def exibirTemperatura(temperatura):
    if isInt(temperatura):
        print(f't°f = {int(temperatura)}')

    else:
        print(f't°f = {temperatura}')    

def converterCelsius(temperatura):
    return (5 * temperatura - 160) / 9

def kmOuKg(valor):
    return valor * 1000

def mParaCm(m):
    return m * 100
    
def m_para_km_e_m(m):
    km = m / 1000
    m_resto = m % 1000
    return [km, m_resto]