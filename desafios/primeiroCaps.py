def uppercase(string):
    result = "" #string vazia que será usada para armazenar o resultado final após as transformações
    capitalize_next = True #controla se o próximo caractere deve ser capitalizado, ou seja, se é o início de uma nova frase

    for char in string:
        if capitalize_next and char.isalpha(): #verifica se capitalize_next é verdadeiro e se o caractere char é uma letra do alfabeto
            char = char.upper()
            capitalize_next = False
        elif char == "." or char == "!" or char == "?": #verifica se o caractere char é um ponto (.), ponto de exclamação (!) ou ponto de interrogação (?)
            capitalize_next = True

        result += char #char é adicionado à string result usando o operador +=.

    return result