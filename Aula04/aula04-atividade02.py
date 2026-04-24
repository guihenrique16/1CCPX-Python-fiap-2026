def validarNota(nota):
    while nota < 0 or nota > 10:
        print('nota entre 0 e 10')
        nota = float(input('digite novamente: '))
    return nota

nA = float(input('Digite a primeira nota: '))
nA = validarNota(nA)

nB = float(input('Digite a segunda nota: '))
nB = validarNota(nB)

media = (nA + nB)/ 2
print(media)

