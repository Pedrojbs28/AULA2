def contar_palavras(texto):
    palavras = texto.split()
    return len(palavras)

def main():
    texto = input("Digite o texto: ")
    resultado = contar_palavras(texto)

    # Escrever resultados em um documento
    with open("resultado_contagem_palavras.txt", "w") as arquivo:
        arquivo.write(f"O número de palavras no texto é: {resultado}")

if __name__ == "__main__":
    main()
