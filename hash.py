import json

def encrypt(plaintext, key):
    """Função para criptografar."""
    encrypted = []
    key_length = len(key)
    
    for i, char in enumerate(plaintext):
        # Obtém o valor da chave correspondente
        key_char = key[i % key_length]
        key_offset = ord(key_char)
        
        # Criptografa o caractere
        encrypted_char = chr((ord(char) + key_offset) % 256)  # Mantém no range de 0 a 255
        encrypted.append(encrypted_char)
    
    return ''.join(encrypted)

def decrypt(ciphertext, key):
    """Função para descriptografar."""
    decrypted = []
    key_length = len(key)
    
    for i, char in enumerate(ciphertext):
        # Obtém o valor da chave correspondente
        key_char = key[i % key_length]
        key_offset = ord(key_char)
        
        # Descriptografa o caractere
        decrypted_char = chr((ord(char) - key_offset) % 256)  # Mantém no range de 0 a 255
        decrypted.append(decrypted_char)
    
    return ''.join(decrypted)

# Mensagem criptografar
mensagem_original = {
    'candidatoA': 10,
    'candidatoB': 30,
    'candidatoC': 15,
    'candidatoD': 25
}

# Chave para criptografia
chave = 'L/ne["W{$PcaK;#.cQ&[G$k)$er=PCf1mlXjqUG`9qm}=+MCT7M=dCH8E[o^%+[)T`JILQBVC3>rLY,oplGlIABGU~LXxGy@zIY=T8bz5,]gsIH6^,#yH04x),49;z$]Ss#,-Ub$rfR@Rx<a(elnCC?)8C6_~zmJWBE1{2PPa7waBd(h*)GQd!~Nrw[{DTIY.:#(Lt`7F`%!qMP)#sYHB|t~HUrwHGTE2#3yzg!yZ2+g6al)QeL[UcCFGLVHqw'

# Converter a mensagem para string JSON
mensagem_original_str = json.dumps(mensagem_original)

# Criptografar a string JSON
mensagem_criptografada = encrypt(mensagem_original_str, chave)
print(f"Mensagem Criptografada: {mensagem_criptografada}")

# Descriptografar a mensagem criptografada
mensagem_descriptografada = decrypt(mensagem_criptografada, chave)

# Converter a string JSON de volta para mensagem original
mensagem_descriptografada_dict = json.loads(mensagem_descriptografada)
print(f"Mensagem Descriptografada: {mensagem_descriptografada_dict}")