import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for i in range(len(plaintext)):
        if (ord(plaintext[i])>=91-shift and ord(plaintext[i])<=90) or (ord(plaintext[i])>=123-shift and ord(plaintext[i])<=122):
            ciphertext+=chr(ord(plaintext[i])-26+shift)
        elif (ord(plaintext[i])>=65 and ord(plaintext[i])<=90 - shift) or (ord(plaintext[i])>=97 and ord(plaintext[i])<=122 - shift):
            ciphertext+=chr(ord(plaintext[i])+shift)
        else:
            ciphertext += plaintext[i]
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for i in range(len(ciphertext)):
        if (ord(ciphertext[i]) >= 65 and ord(ciphertext[i]) <= 64 + shift) or (
                ord(ciphertext[i]) >= 97 and ord(ciphertext[i]) <= 96 + shift):
            plaintext += chr(ord(ciphertext[i]) + 26 - shift)
        elif (ord(ciphertext[i]) >= 65 + shift and ord(ciphertext[i]) <= 90) or (
                ord(ciphertext[i]) >= 97 + shift and ord(ciphertext[i]) <= 122):
            plaintext += chr(ord(ciphertext[i]) - shift)
        else:
            plaintext += (ciphertext[i])
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift

print(encrypt_caesar('xyz', 4))