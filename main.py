from .desafios.reverterOrdem import reverseOrder
from .desafios.removerChar import removeChars
from .desafios.primeiroCaps import uppercase
from .desafios.palindromoLongo import longestPal
from .desafios.anagramaPalindromo import anaPal


def main():
    while True:
        print("MENU:")
        print("0 - Encerrar o programa")
        print("1 - Chamar a função reverseOrder()")
        print("2 - Chamar a função removeChars()")
        print("3 - Chamar a função uppercase()")
        print("4 - Chamar a função longestPal()")
        print("5 - Chamar a função anaPal()")

        opcao = input("Insira um número de 0 a 5: ")

        if opcao == "0":
            print("Encerrando o programa...")
            break
        elif opcao == "1":
            reverseOrder()
        elif opcao == "2":
            removeChars()
        elif opcao == "3":
            uppercase()
        elif opcao == "4":
            longestPal()
        elif opcao == "5":
            anaPal()
        else:
            print("Opção inválida. Insira um número entre 0 e 5.")

if __name__ == "__main__":
    main()