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

# 2. Assinar uma mensagem com a chave privada
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

# 3. Verificar a assinatura com a chave pública
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

    # Gerar as chaves
    private_key, public_key = generate_keys()

    # Mensagem a ser assinada
    message = "Esta é uma mensagem confidencial."
    message_bytes = message.encode('utf-8')

    # Assinar a mensagem
    signature = sign_message(private_key, message_bytes)
    print("Assinatura gerada com sucesso.")

    # Verificar a assinatura
    valid = verify_signature(public_key, message_bytes, signature)
    if valid:
        print("Assinatura verificada e válida.")
    else:
        print("Assinatura inválida.")
