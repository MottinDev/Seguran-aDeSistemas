import hmac
import hashlib

def hmac_auth(key, message):
    #Gera o HMAC usando a chave e a mensagem
    return hmac.new(key.encode('utf-8'), message.encode('utf-8'), hashlib.sha256).hexdigest()

def verify_hmac(key, message, hmac_to_verify):
    #Gera o HMAC para a mensagem e a chave que foram fornecidas
    generated_hmac = hmac_auth(key, message)
    #Compara o HMAC gerado com HMAC fornecido
    return hmac.compare_digest(generated_hmac, hmac_to_verify)

#Exemplo de uso
if __name__ == "__main__":
    key = "Chave_secreta"
    message = "Mensagem_confidencial"

    #Gera o HMAC
    hmac_value = hmac_auth(key, message)
    print(f"HMAC: {hmac_value}")

    #Verificar o HMAC
    hmac_to_verify = hmac_value

    #Verifica se o HMAC é válido
    is_valid = verify_hmac(key, message, hmac_to_verify)
    print(f"O HMAC é válido ? {is_valid}")