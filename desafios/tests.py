# tests.py
import sys
sys.path.append("..")

from desafios.reverterOrdem import reverseOrder
from desafios.removerChar import removeChars
from desafios.primeiroCaps import uppercase
from desafios.palindromoLongo import longestPal
from desafios.anagramaPalindromo import anagPal

def test_reverseOrder():
    print("\n")
    print("##### INICIO DE TESTES #####")
    print("1° Frase: Hello, World! OpenAI is amazing")
    print("2° Frase: Desafio de código da PwC.")
    print("3° Frase: Estes testes hard-coded não são ideais!\n")
           
    print("---Resultados---")

    teste_1 = "Hello, World! OpenAI is amazing!"
    print(reverseOrder(teste_1))
    teste_2 = "Desafio de código da PwC."
    print(reverseOrder(teste_2))
    teste_3 = "Estes testes hard-coded não são ideais!"
    print(reverseOrder(teste_3))
    print("##### FIM DE TESTES #####\n")

##################### REMOVER CARACTERES ##################### 

def test_removeChars():
    # Teste 1: Remover caractéres duplicados
    print("\n")
    print("##### INICIO DE TESTES #####")
    print("1° Teste: Hello, World!")
    print("2° Teste: Desafio de código programado em Python.")
    print("3° Teste: Programming\n")
           
    print("---Resultados---")

    teste_1 = "Hello, World!"
    print(removeChars(teste_1))
    teste_2 = "Desafio de código programado em Python."
    print(removeChars(teste_2))
    teste_3 = "Programming"
    print(removeChars(teste_3))
    print("##### FIM DE TESTES #####\n")



##################### MAIOR PALINDROMO NUMA SUBSTRING ##################### 

def test_longestPal():
    input_string = "level"
    input_string = "noon"
    input_string = "hello"
    # Se não houver palíndromos na string, a função deve retornar o caractere na primeira posição.
    print("\n")
    print("##### INICIO DE TESTES #####")
    print("1° Teste: babad")
    print("2° Teste: cbbd")
    print("3° Teste: iaiasumi\n")
           
    print("---Resultados---")

    teste_1 = "babad"
    print(longestPal(teste_1))
    teste_2 = "cbbd"
    print(longestPal(teste_2))
    teste_3 = "iaiaisumi"
    print(longestPal(teste_3))
    print("##### FIM DE TESTES #####\n")    


##################### CAPITALIZAR PRIMEIRA LETRA #####################

def test_uppercase():
    print("\n")
    print("##### INICIO DE TESTES #####")
    print("1° Teste: hello. how are you? i'm fine.")
    print("2° Teste: [string vazia]")
    print("3° Teste: hello\n")
           
    print("---Resultados---")

    teste_1 = "hello. how are you? i'm fine, thank you"
    print(uppercase(teste_1))
    teste_2 = ""
    print(uppercase(teste_2))
    teste_3 = "this is a sentence. can you tell? i hope so."
    print(uppercase(teste_3))
    print("##### FIM DE TESTES #####\n")  


##################### ANAGRAMA PALINDROMO ##################### 

def test_anagPal():
    print("\n")
    print("##### INICIO DE TESTES #####")
    print("1° Teste: aabbbcc (resultado esperado: True)")
    print("2° Teste: abcde (resultado esperado: False)")
    print("3° Teste: [string vazia] resultado esperado: True\n")
           
    print("---Resultados---")

    teste_1 = "aabbbcc"
    print(anagPal(teste_1))
    teste_2 = "abcde"
    print(anagPal(teste_2))
    teste_3 = ""
    print(anagPal(teste_3))
    print("##### FIM DE TESTES #####\n")  