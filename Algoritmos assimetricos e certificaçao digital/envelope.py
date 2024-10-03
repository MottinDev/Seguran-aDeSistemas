from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import os

# 1. Gerar um par de chaves RSA
def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    return private_key, public_key

# 2. Gerar uma chave simétrica para a criptografia da mensagem
def generate_symmetric_key():
    return os.urandom(32)  # Chave AES de 256 bits

# 3. Cifrar a mensagem usando a chave simétrica (AES)
def cifrar_mensagem_simetrica(mensagem, chave_simetrica):
    iv = os.urandom(16)  # Vetor de inicialização para AES
    cipher = Cipher(algorithms.AES(chave_simetrica), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    mensagem_cifrada = encryptor.update(mensagem.encode('utf-8')) + encryptor.finalize()
    return iv, mensagem_cifrada

# 4. Cifrar a chave simétrica com a chave pública do destinatário
def cifrar_chave_simetrica(chave_simetrica, chave_publica_destinatario):
    chave_simetrica_cifrada = chave_publica_destinatario.encrypt(
        chave_simetrica,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return chave_simetrica_cifrada

# 5. Decifrar a chave simétrica com a chave privada do destinatário
def decifrar_chave_simetrica(chave_simetrica_cifrada, chave_privada_destinatario):
    chave_simetrica = chave_privada_destinatario.decrypt(
        chave_simetrica_cifrada,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return chave_simetrica

# 6. Decifrar a mensagem com a chave simétrica
def decifrar_mensagem_simetrica(iv, mensagem_cifrada, chave_simetrica):
    cipher = Cipher(algorithms.AES(chave_simetrica), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    mensagem_decifrada = decryptor.update(mensagem_cifrada) + decryptor.finalize()
    return mensagem_decifrada.decode('utf-8')

# Exemplo de uso
if __name__ == "__main__":
    # Gerar as chaves do remetente e do destinatário
    remetente_private_key, remetente_public_key = generate_keys()
    destinatario_private_key, destinatario_public_key = generate_keys()

    # Mensagem a ser enviada
    mensagem_original = "Mensagem confidencial com envelope criptográfico."

    # Gerar a chave simétrica
    chave_simetrica = generate_symmetric_key()

    # Cifrar a mensagem com a chave simétrica
    iv, mensagem_cifrada = cifrar_mensagem_simetrica(mensagem_original, chave_simetrica)
    
    # Cifrar a chave simétrica com a chave pública do destinatário
    chave_simetrica_cifrada = cifrar_chave_simetrica(chave_simetrica, destinatario_public_key)

    # Decifrar a chave simétrica com a chave privada do destinatário
    chave_simetrica_decifrada = decifrar_chave_simetrica(chave_simetrica_cifrada, destinatario_private_key)

    # Decifrar a mensagem com a chave simétrica decifrada
    mensagem_decifrada = decifrar_mensagem_simetrica(iv, mensagem_cifrada, chave_simetrica_decifrada)
    
    print(f"Mensagem decifrada: {mensagem_decifrada}")
