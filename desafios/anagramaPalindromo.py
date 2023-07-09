from collections import Counter #counter será utilizado para contar a ocorrência de cada caractere em uma string

def anagPal(string):
   c = Counter(string) #'c' inicia como um objeto Counter criado a partir da string. Isso conta a ocorrência de cada caractere na string e armazena essas contagens no objeto 'c'.
   count = 0
   for i in c.values(): #Dentro do loop, é verificado se a contagem 'i' é ímpar 
      if i % 2 != 0:
         if count == 0:
            count += 1
            continue
         return False
   return True

