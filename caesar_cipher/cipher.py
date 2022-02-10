# import nltk
from caesar_cipher.corpus import name_list, word_list
# import string
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


def crack(encrypted):
  # loop through each option
    for i in range(26):
      # star the word counter at 0
        word_count = 0
        # the variable words implements the encrypted function that takes in encrypted and i as arguments
        words = encrypt(encrypted, i)
        # the list is equal to the split of the encrypted sentence into separate words
        list = words.split()
        for text in list:
          # iterate throughout each word.
          #if there is a match either in the name list or the word list it will increase the counter by 1.
            if text in name_list or text.lower() in word_list:
                word_count += 1
       # then check if the current word count is greater than 50% if so join all  the words together 
        if (word_count/len(list)) > .5:
            return " ".join(list)
            # if the word list count is not greater than 50% return just an empty string 
    return ""


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

if __name__ == "__main__":
    enc1 = encrypt('12345', 2)
    assert enc1 == ('34567')

    # enc2 = encrypt('678', 2)
    # assert enc2 == ('890')

    # enc3 = encrypt('1234', 28374)
    # print(enc3)

    enc4 = decrypt('34567', 2)
    assert enc4 == '12345'