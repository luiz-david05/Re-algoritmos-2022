# testando import 
def hello() :
    nome = input('digite seu nome: ')
    print(f'\t--- {nome}, seja bem-vindo!---')

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

def area_triangulo(base, altura):
    return (base * altura) / 2 

def quadrado(n):
    return n * n    