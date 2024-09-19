import hmac
import hashlib
import os

def generate_random_bytes(length):
    # Gera o tamanho bytes aleatórios
    return os.urandom(length)

def hmac_auth(key, message):
    # Gera o HMAC usando a chave de bytes e a mensagem
    return hmac.new(key, message.encode('utf-8'), hashlib.sha256).hexdigest()

def verify_hmac(key, message, hmac_to_verify):
    # Gera o HMAC para a mensagem e a chave que foram fornecidas
    generated_hmac = hmac_auth(key, message)
    # Compara o HMAC gerado com o HMAC fornecido
    return hmac.compare_digest(generated_hmac, hmac_to_verify)

# Exemplo de uso
if __name__ == "__main__":
    message = "Mensagem_confidencial"
    
    # Gera uma chave aleatória de 16 bytes
    key = generate_random_bytes(16)
    print(f"Chave Aleatória (bytes): {key}")

    # Gera o HMAC usando a chave aleatória
    hmac_value = hmac_auth(key, message)
    print(f"HMAC: {hmac_value}")

    # Verifica o HMAC
    hmac_to_verify = hmac_value

    # Verifica se o HMAC é válido
    is_valid = verify_hmac(key, message, hmac_to_verify)
    print(f"O HMAC é válido? {is_valid}")
