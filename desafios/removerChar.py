def removeChars():
    frase =  str(input(''))
    output = ""
    for char in frase:
        if char not in output:
            output = output + char
    print(output) 
