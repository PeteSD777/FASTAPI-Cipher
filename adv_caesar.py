# Function cipher_encrypt is responsible for encoding entered value for the first time,
# by using edited caesar algorithm that uses numerical values

def cipher_encrypt(plain_text):

    # enc value is going to be the ciphered value
    enc = ""
    # firstly, the function loops through it's argument
    for i in plain_text:
        # if index is character and in upperCase then  it shifts it's the upperCase value
        if i.isupper():
            i_index = ord(i)-ord('A')
            i_shift = (i_index + 5) % 26+ord('A')
            i_new = chr(i_shift)
            enc += i_new
        # if index is character and not in upperCase then it shifts the lowercase value
        elif i.islower():
            i_index = ord(i)-ord('a')
            i_shift = (i_index+5) % 26+ord('a')
            i_new = chr(i_shift)
            enc += i_new
        # if index is digit, it shifts the index value by 5
        elif i.isdigit():
            i_new = (int(i)+5) % 10
            enc += str(i_new)
        else:
            enc += i
    # funciton returns ciphered value
    return enc

# Function cipher_decrypt is responsible for decoding value encoded by cipher_encrypt


def cipher_decrypt(ciphertext):
    # decrypt value is going  to be the decoded value
    decrypt = ""
    # firstly, the function loops through it's argument
    for i in ciphertext:
        # if index is character and in UpperCase then it shifts index value back to the original state
        if i.isupper():
            i_index = ord(i)-ord('A')
            i_original_position = (i_index - 5) % 26 + ord('A')
            i_original = chr(i_original_position)
            decrypt += i_original
    # if index is characted and in lowerCase then it shifts index value back to the original state
        elif i.islower():
            i_index = ord(i)-ord('a')
            i_original_position = (i_index - 5) % 26 + ord('a')
            i_original = chr(i_original_position)
            decrypt += i_original
    # if index is digit then it shifts index value back to the orignal state
        elif i.isdigit():
            i_original = (int(i)-5) % 10
            decrypt += str(i_original)
        else:
            decrypt += i
    # function returns orignal value
    return decrypt
