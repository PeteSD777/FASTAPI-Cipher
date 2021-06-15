import unittest

from adv_caesar import cipher_encrypt, cipher_decrypt
from crypto import encodeFunction, decodeFunction


class TestCipherOneEncrypt(unittest.TestCase):
    def test(self):
        """
        test that cipher_encrypt can encrypt phrases
        """

        data = "peter123"
        cipher = cipher_encrypt(data)
        result = cipher_decrypt(cipher)

        self.assertEqual(result, data)


class TestEncodeDecodeTwoFunction(unittest.TestCase):
    def test_second_functions(self):
        """
        test that encodeFunction and decode function are encoding and decoding taken values

        """

        data = "peter123"
        test_db = []
        cipher = cipher_encrypt(data)
        resultencode = encodeFunction(data)
        test_db.append(resultencode)
        resultdecode = decodeFunction(test_db[0])

        self.assertEqual(resultdecode, data)


if __name__ == '__main__':
    unittest.main()
