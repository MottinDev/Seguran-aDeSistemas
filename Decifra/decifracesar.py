def cifracesar(texto, chave):
    resultado = ""
    # Iterando o texto
    for i in range(len(texto)):
        char = texto[i]
        # Letras maiúsculas
        if char.isupper():
            resultado += chr((ord(char) - 65 - chave) % 26 + 65)
        # Letras minúsculas
        elif char.islower():
            resultado += chr((ord(char) - 97 - chave) % 26 + 97)
        # Outros caracteres
        else:
            resultado += char
    return resultado

def main():
    while True:
        # Solicitando o texto e a chave do usuário
        meuTexto = input("Digite o texto que deseja decifrar: ")
        chave = int(input("Digite a chave (número inteiro): "))
        
        # Decifrando o texto
        resultado = cifracesar(meuTexto, chave)
        print(f"Texto decifrado: {resultado}")
        
        # Perguntando ao usuário se deseja continuar
        continuar = input("Deseja decifrar outro texto? (s/n): ").lower()
        if continuar != 's':
            print("Saindo...")
            break

# Chamando a função principal
if __name__ == "__main__":
    main()
