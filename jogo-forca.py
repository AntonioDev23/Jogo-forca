import random

# Lista de palavras para o jogo
palavras = ["python", "programacao", "desenvolvimento", "algoritmo", "computador"]

# Escolhe uma palavra aleatória
palavra_secreta = random.choice(palavras)

# Número máximo de tentativas
tentativas_maximas = 6

# Letras já tentadas pelo jogador
letras_tentadas = []

# Progresso do jogador (underscores representam letras não adivinhadas)
progresso = ["_"] * len(palavra_secreta)

# Função para exibir o progresso atual
def exibir_progresso():
    print(" ".join(progresso))

# Função principal do jogo
def jogo_da_forca():
    tentativas = 0

    print("Bem-vindo ao Jogo da Forca!")
    print(f"A palavra tem {len(palavra_secreta)} letras.")
    exibir_progresso()

    while tentativas < tentativas_maximas:
        letra = input("\nDigite uma letra: ").lower()

        # Verifica se a letra já foi tentada
        if letra in letras_tentadas:
            print("Você já tentou essa letra. Tente outra!")
            continue

        letras_tentadas.append(letra)

        # Verifica se a letra está na palavra secreta
        if letra in palavra_secreta:
            print(f"Boa! A letra '{letra}' está na palavra.")
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == letra:
                    progresso[i] = letra
        else:
            print(f"Ops! A letra '{letra}' não está na palavra.")
            tentativas += 1

        # Exibe o progresso atual
        exibir_progresso()

        # Verifica se o jogador ganhou
        if "_" not in progresso:
            print("\nParabéns! Você acertou a palavra!")
            break

        # Exibe o número de tentativas restantes
        print(f"Tentativas restantes: {tentativas_maximas - tentativas}")

    # Verifica se o jogador perdeu
    if tentativas == tentativas_maximas:
        print(f"\nGame over! A palavra era: {palavra_secreta}")

# Inicia o jogo
jogo_da_forca()