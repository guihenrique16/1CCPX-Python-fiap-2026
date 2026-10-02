palavras = {
    "frutas": ["banana", "morango", "abacaxi", "melancia"],
    "cores": ["azul", "verde", "amarelo", "vermelho"],
    "animais": ["cachorro", "gato", "elefante", "girafa"]
}

print("=" * 40)
print("       JOGO DE ADIVINHAÇÃO")
print("=" * 40)

print("\nEscolha uma categoria:")

categorias = list(palavras.keys())

for i in range(len(categorias)):
    print(f"{i + 1} - {categorias[i].capitalize()}")

opcao = int(input("\nDigite a opção: "))

while opcao < 1 or opcao > len(categorias):
    print("Opção inválida.")
    opcao = int(input("Digite novamente: "))

categoria_escolhida = categorias[opcao - 1]

lista_palavras = palavras[categoria_escolhida]

print(f"\nA categoria possui {len(lista_palavras)} palavras.")

posicao = int(input("Escolha a posição da palavra: "))

while posicao < 1 or posicao > len(lista_palavras):
    print("Posição inválida.")
    posicao = int(input("Escolha novamente: "))

palavra_secreta = lista_palavras[posicao - 1]

palavra_descoberta = ["_"] * len(palavra_secreta)

tentativas = 6

letras_digitadas = []

print("\nPalavra:", " ".join(palavra_descoberta))

print("\nVocê terá 6 tentativas para descobrir a palavra.")

while tentativas > 0 and "_" in palavra_descoberta:

    print("\n" + "=" * 40)

    print("Palavra:", " ".join(palavra_descoberta))

    print(f"Tentativas restantes: {tentativas}")

    if letras_digitadas:
        print("Letras utilizadas:", ", ".join(letras_digitadas))

    letra = input("Digite uma letra: ").lower()

    if len(letra) != 1 or not letra.isalpha():
        print("Digite apenas uma letra.")
        continue

    if letra in letras_digitadas:
        print("Você já tentou essa letra.")
        continue

    letras_digitadas.append(letra)

    if letra in palavra_secreta:

        print("Você acertou!")

        for i in range(len(palavra_secreta)):

            if palavra_secreta[i] == letra:
                palavra_descoberta[i] = letra

    else:

        tentativas -= 1

        print("Você errou!")
        print(f"Tentativas restantes: {tentativas}")


print("\n" + "=" * 40)

if "_" not in palavra_descoberta:

    print("Palavra:", "".join(palavra_descoberta))

    print(f"\nParabéns! Você descobriu a palavra: {palavra_secreta}")

else:

    print("Suas 6 tentativas terminaram.")
    print(f"A palavra era: {palavra_secreta}")

print("=" * 40)