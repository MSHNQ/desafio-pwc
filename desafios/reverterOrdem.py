def reverseOrder(frase):
    splitting = frase.split()[::-1] #divide a string frase em uma lista de palavras usando o espaço em branco como separador. [::-1] cria uma nova lista com a ordem invertida das palavras.
    auxList = []
    for i in splitting: #Dentro do loop, cada palavra i é adicionada à lista auxList
        auxList.append(i)
    return (" ".join(auxList))