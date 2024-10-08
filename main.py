import comprimento
import massa
import volume
def main():
    """
    Função principal do programa.
    """
    while True:  # Laço infinito
        print("#######################################################")
        print("## CALCULADORA DO SISTEMAS INTERNACIONAL DE UNIDADES ##")
        print("#######################################################")

        print("\nEscolha uma conversão:")
        print("1. Comprimento (m para km)")
        print("2. Comprimento (km para m)")
        print("3. Massa (g para kg)")
        print("4. Massa (kg para g)")
        print("5. Volume (l para ml)")
        print("6. Volume (ml para l)")
        print("0. Sair")

        escolha = input("Digite sua escolha: ")

        if escolha == "0":  # Sai do programa quando a escolha é 0
            print("Saindo do programa.")
            break

        if escolha == "1":
            metros = float(input("Digite o valor em metros: "))
            quilometros = comprimento.metro_km(metros)
            print(f"{metros} metros são {quilometros} quilômetros.")
            break
            
        elif escolha == "2":
            quilometros = float(input("Digite o valor em quilômetros: "))
            metros = comprimento.km_metro (quilometros)
            print(f"{quilometros} quilômetros são {metros} metros.")
            break

        elif escolha == "3":
            gramas = float(input("Digite o valor em gramas: "))
            quilogramas = massa.grama(gramas)
            print(f"{gramas} gramas são {quilogramas} quilogramas.")
            break
           
        elif escolha == "4":
            quilogramas = float(input("Digite o valor em quilogramas: "))
            gramas = massa.kg(quilogramas)
            print(f"{quilogramas} quilogramas são {gramas} gramas.")
            break

        elif escolha == "5":
            litros = float(input("Digite o valor em litros: "))
            mililitros = volume.litros(litros)
            print(f"{litros} litros são {mililitros} mililitros.")
            break

        elif escolha == "6":
            mililitros = float(input("Digite o valor em mililitros: "))
            litros = volume.mililitros(mililitros)
            print(f"{mililitros} mililitros são {litros} litros.")
            break

        else:
            print("Escolha inválida. Por favor, tente novamente.")

# ----------------------------------------------------------------------------------------
if __name__ == "__main__":  # Garante que se o módulo for importado não será executado
    main()  # Chamada da função principal
