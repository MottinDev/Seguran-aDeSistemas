import os

def generate_random_bytes(length):
    return os.urandom(length).hex()

#Exemplo de uso
random_value = generate_random_bytes(16)

#16 bytes aleatórios
print(f"Numero Aleatorio: {random_value}")