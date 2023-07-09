import sys
sys.path.insert(0, '.')  

from testes.tests import test_reverseOrder, test_removeChars, test_longestPal, test_uppercase, test_anagPal


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
            test_reverseOrder()
        elif opcao == "2":
            test_removeChars()
        elif opcao == "3":
            test_uppercase()
        elif opcao == "4":
            print(test_longestPal())
        elif opcao == "5":
            print(test_anagPal())
        else:
            print("Opção inválida. Insira um número entre 0 e 5.")

if __name__ == "__main__":

    main()