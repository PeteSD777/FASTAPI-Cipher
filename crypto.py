from cryptography.fernet import Fernet
from adv_caesar import cipher_encrypt, cipher_decrypt
key = Fernet.generate_key()
f = Fernet(key)

# function encodeFunction is responsible for the second encoding of the value.


def encodeFunction(inputValue):
    # firstly, this function will take the output of cipher_encrypt function, and assign it to the caesar_value
    caesar_value = cipher_encrypt(inputValue)
    # secondly, the encodeFunction will encode the value assigned to caesar_value
    byte = str.encode(caesar_value)
    # encodeFunction will use the Fernet cipher-algorithm to assign a value to a token
    token = f.encrypt(byte)

    return token

# function decodeFunction is responsible for the complete encoding of dual-encoded value


def decodeFunction(database_id):
    # this function will decode the value selected by id of said value, decoding is first performed by fernet decoder
    decode = f.decrypt(database_id)
    # decode function will then take the fernet decoded value and pass it through cipher_decrypt to decode it from the ceasrian-encoding with numbers

    caesar_decode = cipher_decrypt(decode.decode("utf-8"))

    return caesar_decode
