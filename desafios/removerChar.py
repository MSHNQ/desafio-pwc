def removeChars(frase):
    output = "" #iniciada como vazia
    for char in frase:
        if char not in output: #verifica se a caractere está presente em output; se não, é adicionado a ela; repetidas não são adicionadas.
            output = output + char
    return output
