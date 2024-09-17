from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def aes_encriptar(mensagem, chave):
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(chave, AES.MODE_CBC, iv)
    mensagem_padded = pad(mensagem.encode("utf-8"), AES.block_size)

    mensagem_encriptada = cipher.encrypt(mensagem_padded)

    return iv + mensagem_encriptada

def aes_decriptar(mensagem_encriptada, chave):
    iv = mensagem_encriptada[:AES.block_size]
    cipher = AES.new(chave, AES.MODE_CBC, iv)
    mensagem_padded = cipher.decrypt(mensagem_encriptada[AES.block_size:])
    mensagem = unpad(mensagem_padded, AES.block_size)
    return mensagem.decode("utf-8")

# Solicitando entrada do usuário
mensagem = input("Digite a mensagem que deseja criptografar: ")
chave = get_random_bytes(16)  # Gerando uma chave aleatória de 16 bytes (128 bits)

# Criptografando a mensagem
mensagem_encriptada = aes_encriptar(mensagem, chave)
print(f"Mensagem criptada: {mensagem_encriptada.hex()}")  # Mostrando a mensagem criptada em hexadecimal

# Descriptografando a mensagem
mensagem_decriptada = aes_decriptar(mensagem_encriptada, chave)
print(f"Mensagem decifrada: {mensagem_decriptada}")
