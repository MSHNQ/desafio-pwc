def reverseOrder():
    frase =  str(input(''))
    splitting = frase.split()[::-1]
    auxList = []
    for i in splitting:
        auxList.append(i)
    print(" ".join(auxList))