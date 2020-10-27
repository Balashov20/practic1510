def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    length = len(keyword)
    for i in range(len(keyword), len(plaintext)):
        keyword += keyword[i - length]
    keyword1 = keyword.lower()
    for i in range(len(plaintext)):
        shift = ord(keyword1[i]) - 97
        if (ord(plaintext[i]) >= 91 - shift and ord(plaintext[i]) <= 90) or (
                ord(plaintext[i]) >= 123 - shift and ord(plaintext[i]) <= 122):
            ciphertext += chr(ord(plaintext[i]) - 26 + shift)
        elif (ord(plaintext[i]) >= 65 and ord(plaintext[i]) <= 90 - shift) or (
                ord(plaintext[i]) >= 97 and ord(plaintext[i]) <= 122 - shift):
            ciphertext += chr(ord(plaintext[i]) + shift)
        else:
            ciphertext += plaintext[i]

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    length = len(keyword)
    for i in range(len(keyword), len(ciphertext)):
        keyword += keyword[i - length]
    keyword1 = keyword.lower()
    for i in range(len(ciphertext)):
        shift = ord(keyword1[i]) - 97
        if (ord(ciphertext[i]) >= 65 and ord(ciphertext[i]) <= 64 + shift) or (
                ord(ciphertext[i]) >= 97 and ord(ciphertext[i]) <= 96 + shift):
            plaintext += chr(ord(ciphertext[i]) + 26 - shift)
        elif (ord(ciphertext[i]) >= 65 + shift and ord(ciphertext[i]) <= 90) or (
                ord(ciphertext[i]) >= 97 + shift and ord(ciphertext[i]) <= 122):
            plaintext += chr(ord(ciphertext[i]) - shift)
        else:
            plaintext += (ciphertext[i])
    return plaintext

print(encrypt_vigenere("PYTHON", "A"))
