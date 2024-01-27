'''
Max Chalitsios 1808500
Cryptography Practice - Caeser Cipher
''' 
def crypt(plaintext:str="", shift_value:int=0, encrypt:bool=True) -> str:
    result = ""
    shift = shift_value if encrypt else -shift_value
    for i in range(len(plaintext)):
        char = plaintext[i]
        if char.isalpha():
            if (char.isupper()):
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

if __name__ == '__main__':
    shift_value = 4
    plaintext = "ATTACK AT ONCE"
    print("Plaintext: ", plaintext)
    ciphertext = crypt(plaintext, shift_value, True)
    print("Ciphertext:", ciphertext)
    decryptedtext = crypt(ciphertext, shift_value, False)
    print("Decrypting:", decryptedtext)
    
    