from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

# Gerar um par de chaves (pública e privada)
def gerar_chaves():
    chave_privada = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    chave_publica = chave_privada.public_key()
    
    return chave_privada, chave_publica

# Função para cifrar a mensagem com a chave pública
def cifrar_mensagem(mensagem, chave_publica):
    mensagem_bytes = mensagem.encode('utf-8')
    mensagem_cifrada = chave_publica.encrypt(
        mensagem_bytes,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return mensagem_cifrada

# Função para decifrar a mensagem com a chave privada
def decifrar_mensagem(mensagem_cifrada, chave_privada):
    mensagem_decifrada = chave_privada.decrypt(
        mensagem_cifrada,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return mensagem_decifrada.decode('utf-8')

# Exemplo
chave_privada, chave_publica = gerar_chaves()

mensagem_original = "Esta é uma mensagem confidencial."
print("Mensagem original:", mensagem_original)

# Cifrar a mensagem
mensagem_cifrada = cifrar_mensagem(mensagem_original, chave_publica)
print("Mensagem cifrada:", mensagem_cifrada)

# Decifrar a mensagem
mensagem_decifrada = decifrar_mensagem(mensagem_cifrada, chave_privada)
print("Mensagem decifrada:", mensagem_decifrada)
