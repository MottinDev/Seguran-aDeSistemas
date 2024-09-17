# Importando bibliotecas
from PIL import Image

# Converte uma string de texto em binário usando codificação ASCII
def textoParaBinario(texto):
    return ''.join(format(ord(c), '08b') for c in texto)

# Solicitando entrada do usuário para o arquivo de imagem e texto
print('Digite o nome do arquivo de imagem a ser aberto:')
imagemEntrada = input()
print('Digite o texto a ser codificado:')
textoEntrada = input()
print('Digite o nome do arquivo de imagem para salvar:')
imagemSaida = input()

# Convertendo a mensagem de texto em binário
mensagemBinaria = textoParaBinario(textoEntrada)

# Carregando os dados de pixels da imagem
imagem = Image.open(imagemEntrada)
largura, altura = imagem.size
pixels = imagem.load()

# Alterando o bit menos significativo de cada pixel para codificar a mensagem
bitAtual = 0
for x in range(largura):
    if bitAtual >= len(mensagemBinaria):
        break

    # Obtendo o pixel atual
    pixelAtual = pixels[x, 0]

    # Modificando os valores de R, G e B do pixel
    novoPixel = list(pixelAtual)
    for cor in range(3):  # Percorrendo os canais de cor (R, G, B)
        if bitAtual >= len(mensagemBinaria):
            break
        corBinaria = format(pixelAtual[cor], '08b')  # Convertendo o valor da cor para binário de 8 bits
        corBinaria = list(corBinaria)
        corBinaria[7] = mensagemBinaria[bitAtual]  # Alterando o bit menos significativo
        novoPixel[cor] = int(''.join(corBinaria), 2)  # Convertendo de volta para inteiro

        bitAtual += 1

    # Substituindo o pixel antigo pelo novo
    pixels[x, 0] = tuple(novoPixel)

# Salvando a nova imagem com a mensagem codificada
imagem.save(imagemSaida)

print("Mensagem codificada e imagem salva com sucesso!")
