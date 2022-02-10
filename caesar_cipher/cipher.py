# import nltk

# nltk.download()

# IWT FJXRZ QGDLC UDM YJBETS DKTG IWT APOXAN HATTEXCV SDV
# THE QUICK BROWN FOX JUMPED OVER THE LAZYLY SLEEPING DOG

#A python program to illustrate Caesar Cipher Technique
def encrypt(text,key):
    encrypted_text = ""
 
    # traverse text
    for i in range(len(text)):
        char = text[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            encrypted_text += chr((ord(char) + key-65) % 26 + 65)
        elif char == ' ':
          encrypted_text += char
        # Encrypt lowercase characters
        elif(char.islower()):
            encrypted_text += chr((ord(char) + key - 97) % 26 + 97)
        else:
          encrypted_text += char
 
    return encrypted_text

def decrypt(encrypted, key):
    return encrypt(encrypted, -key)


# def encrypt(plain, key):
#     # plain: '12345'
#     # key: 2
#     # -> '34567'
#     encrypted_text = ''

#     for char in plain:
#         # print(f'plain char of {char} not yet shifted by {key}')
#         encrypted_char = int(char)
#         encrypted_char += key
#         # 10 -> 0
#         # 11 -> 1
#         if encrypted_char > 9:
#             encrypted_char = encrypted_char %10
#         # print(f'encrypted char of {encrypted_char} shifted by {key}')
#         encrypted_text += str(encrypted_char)
#     return encrypted_text
#     # shift the plain text
#     # store the shifted value
#     # return the shifted value

# def decrypt(encrypted, key):
#     return encrypt(encrypted, -key)

def crack(encrypted):
    pass

if __name__ == "__main__":
    enc1 = encrypt('12345', 2)
    assert enc1 == ('34567')

    # enc2 = encrypt('678', 2)
    # assert enc2 == ('890')

    # enc3 = encrypt('1234', 28374)
    # print(enc3)

    enc4 = decrypt('34567', 2)
    assert enc4 == '12345'