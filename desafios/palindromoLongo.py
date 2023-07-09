def longestPal(string):
    n = len(string)
    if (n < 2): #. Se o comprimento for menor que 2, significa que não é possível formar um palíndromo
        return n                  
                 
    start=0 #guarda o índice de início do palíndromo mais longo encontrado até o momento
    maxLength = 1 #guarda o comprimento desse palíndromo
    for i in range(n):
        low = i - 1 #representa o índice à esquerda de 'i'
        high = i + 1 #representa o índice à direita de 'i'
        while (high < n and string[high] == string[i] ): #primeiro loop percorre para a direita, enquanto high é menor que o comprimento da string 
            high=high+1                                                                                                 #e o caractere em 'high' é igual ao caractere em 'i'                             
       
        while (low >= 0 and string[low] == string[i] ):#segundo loop percorre para a esquerda, enquanto 'low' é maior ou igual 
            low=low-1                                                                                           #a zero e o caractere em low é igual ao caractere em 'i'             
       
        while (low >= 0 and high < n and string[low] == string[high] ): #ultimo loop percorre para a esquerda e para a direita simultaneamente, 
          low=low-1                                                              #comparando os caracteres em low e high até que eles não sejam mais iguais ou alcancem 
          high=high+1                                                                                  #os limites da string. Isso ajuda a encontrar a parte central do palíndromo.
         
     
        length = high - low - 1 #comprimento do palíndromo é calculado como a diferença entre high e low
        if (maxLength < length):
            maxLength = length
            start=low+1
             
    print ("O palindromo mais longo da substring é:",end=" ")
    print (string[start:start + maxLength])
     
    return maxLength
