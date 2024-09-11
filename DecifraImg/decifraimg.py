# Importando bibliotecas
from PIL import Image

# Converte uma string binária em texto usando codificação ASCII
def binarioParaTexto(binStr):
    texto = ''
    for i in range(0, len(binStr) // 8):
        texto += chr(int(binStr[i*8:i*8+8], 2))
    return texto

# Obtendo entrada do usuário para o arquivo de imagem
print('Digite o nome da imagem a ser decodificada:')
imagemEntrada = input()
print('Digite o número de caracteres a decodificar:')
numCaracteres = int(input())
numBits = numCaracteres * 8  # Calcula o número de bits com base na quantidade de caracteres

# Carregando os dados dos pixels da imagem
imagem = Image.open(imagemEntrada)
largura, altura = imagem.size
pixels = imagem.load()

# Extraindo o bit menos significativo (LSB) de cada pixel
binStr = ''
bitAtual = 0
for x in range(largura):
    if bitAtual >= numBits:
        break

    # Obtendo o pixel atual
    pixelAtual = pixels[x, 0]

    # Extraindo os bits das cores R, G, e B
    for cor in range(3):
        if bitAtual >= numBits:
            break
        corBinaria = format(pixelAtual[cor], '08b')  # Converte o valor da cor para binário de 8 bits
        binStr += corBinaria[-1]  # Adiciona o LSB ao binStr

        bitAtual += 1

# Convertendo a string binária para texto e exibindo o resultado
print("Mensagem decodificada:")
print(binarioParaTexto(binStr))
