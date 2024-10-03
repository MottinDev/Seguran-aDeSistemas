from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# 1. Gerar um par de chaves RSA 
def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    return private_key, public_key

# 2. Cifrar a mensagem com a chave pública do destinatário 
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

# 3. Decifrar a mensagem com a chave privada do destinatário
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

# 4. Assinar a mensagem com a chave privada do remetente 
def sign_message(private_key, message):
    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

# 5. Verificar a assinatura com a chave pública do remetente
def verify_signature(public_key, message, signature):
    try:
        public_key.verify(
            signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception as e:
        print(f"Verificação falhou: {e}")
        return False

# Exemplo de uso
if __name__ == "__main__":

    # Gerar as chaves do remetente e do destinatário 
    remetente_private_key, remetente_public_key = generate_keys()
    destinatario_private_key, destinatario_public_key = generate_keys()

    # Mensagem a ser enviada
    mensagem_original = "Esta é uma mensagem confidencial e assinada."
    mensagem_bytes = mensagem_original.encode('utf-8')

    # Assinar a mensagem 
    assinatura = sign_message(remetente_private_key, mensagem_bytes)
    print("Assinatura gerada com sucesso.")

    # Cifrar a mensagem 
    mensagem_cifrada = cifrar_mensagem(mensagem_original, destinatario_public_key)
    print("Mensagem cifrada com sucesso.")

    # Decifrar a mensagem 
    mensagem_decifrada = decifrar_mensagem(mensagem_cifrada, destinatario_private_key)
    print(f"Mensagem decifrada: {mensagem_decifrada}")

    # Verificar a assinatura 
    assinatura_valida = verify_signature(remetente_public_key, mensagem_bytes, assinatura)
    if assinatura_valida:
        print("Assinatura verificada e válida.")
    else:
        print("Assinatura inválida.")
