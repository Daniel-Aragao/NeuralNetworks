import random

def multEscalar(vet1, vet2):
    t = 0

    for i, item in enumerate(vet1):
        t += item * vet2[i]
    
    return t

def multPorEscalar(escalar, vetor):
    return [escalar * item for item in vetor]

def somaVetores(vet1, vet2):
    return [item1 + vet2[i] for i, item1 in enumerate(vet1)]

def fi(pesos, entrada):
    return 1 if multEscalar(pesos, entrada) > 0 else 0

def getVetorErros(entradas,pesos):
    erros = []

    for entrada in entradas:
        saida_desejada = entrada[3]
        erro = saida_desejada - fi(pesos, entrada)
        erros.append(erro)

    return erros

def EQM(entradas, pesos):
    erros = getVetorErros(entradas,pesos)
    return multEscalar(erros, erros)

def randomInterval(a,b):
    return (random.random() * b) - a

pesos = [
    randomInterval(-1, 1),
    randomInterval(-1, 1),
    randomInterval(-1, 1)]

porta_and = [
    [-1,0,0,0],
    [-1,1,0,0],
    [-1,0,1,0],
    [-1,1,1,1]
]

porta_nor = [
    [-1,0,0,1],
    [-1,1,0,0],
    [-1,0,1,0],
    [-1,1,1,0]
]

entradas = porta_nor
learning_rate = 0.1
cont = 0
eras = 0

while True:
    entrada = entradas[cont]

    cont += 1

    saida_desejada = entrada[3]

    erro = saida_desejada - fi(pesos, entrada)
    
    erro_entrada = multPorEscalar(erro, entrada)
    
    pesos = somaVetores(pesos, multPorEscalar(learning_rate, erro_entrada))

    if cont is len(entradas):
        cont = 0
        eras += 1 
        print(pesos)
        if EQM(entradas, pesos) <= 0:
            break

for entrada in entradas:
    print(entrada[1],entrada[2],fi(pesos,entrada))

print("épocas: " + str(eras))