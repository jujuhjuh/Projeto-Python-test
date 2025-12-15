nome = input("Digite seu nome completo: ")

while True:
    try:
        ano_nascimento = int(input("Digite seu ano de nascimento: "))

        if 1922 <= ano_nascimento <= 2021:
            idade = 2022 - ano_nascimento
            print(f"\nNome: {nome}")
            print(f"Idade em 2022: {idade} anos")
            break
        else:
            print("Erro: o ano deve estar entre 1922 e 2021.")

    except ValueError:
        print("Erro: digite um número válido para o ano.")