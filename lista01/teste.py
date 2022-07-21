# testando import 
def hello() :
    nome = input('digite seu nome: ')
    print(f'\t--- {nome}, tomar no teu cu, rapá!---')

def ehInt(n):
     return n % 1 == 0 

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
    if ehInt(area):
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
    if ehInt(temperatura):
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

def dias_para_semanas_e_dias(dias):
    semanas = dias / 7
    resto_dias = dias % 7
    return [semanas, resto_dias]

def segundos_para_hr_min_segs(segundos):
    horas = segundos / 3600
    minutos = (segundos / 60) % 60
    segundos_resto = segundos % 60
    
    return [horas, minutos, segundos_resto]

def horas_para_semanas_dias_horas(horas):
    hrs_semana = 24 * 7
    semanas = horas / hrs_semana
    dias = (horas / 24) % 24
    horas_resto = horas % 24
    
    return [semanas, dias, horas_resto]

def meses_para_anos_e_meses(meses):
    anos = meses / 12
    resto_meses = meses % 12
    
    return [anos, resto_meses]

def horas_para_dias_horas_e_minutos(minutos):
    dias = minutos / (24 * 60)
    horas = (minutos % 1440) / 60
    resto_minutos = minutos % 60
    
    return [dias, horas, resto_minutos]

def converterBinarioParaDecimal(binario):
    n = len(str(binario))
    decimal = 0
    i = 0

    while n >= 0:
        resto = binario % 10
        decimal = decimal + (resto * (2**i))
        n -= 1
        i += 1
        binario //=  10
    
    return decimal

def n_inverso(n):
    c = n // 100
    d = (n % 100) // 10
    u = n % 10
    
    return c, d, u

def mediaAritmetica(n1, n2, n3):
    return (n1 + n2 + n3) / 3

def somar_elementos_n_4digitos(n):
    m = n // 1000
    c = (n % 1000) // 100
    d = (n % 100) // 10
    u = n % 10
    
    soma = m + c + d + u
    print(f'soma == {m} + {c} + {d} + {u} = {soma} ')
    
def IdadeEmDias(anos, meses, dias):
    anos_dias = anos * 365
    meses_dias = meses * 30
    
     # não ira cobrir os anos bissextos
    idade_dias = anos_dias + meses_dias + dias
    
    return idade_dias