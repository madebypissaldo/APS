def caesar_crypt(text, shift):
    result = ''
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char
    return result

senha = 'Gabriel'
shift = 4

crypto = caesar_crypt(senha, shift)

decrypt = caesar_decrypt(crypto, shift)

print(crypto)
print(decrypt)