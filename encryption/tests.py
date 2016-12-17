import module
import os
import sys
import unittest


class TestEncryptuin(unittest.TestCase):

    def setUp(self):
        self.message = 'ABC'
        self.key = '1234567890123456'

    def test_symEncrypt(self):
        message1 = 'MSG'
        encrypted_message = module.symEncrypt(message1, self.key)
        message2 = module.symDecrypt(encrypted_message, self.key)
        self.assertEqual(message1, message2)
        message3 = module.symDecrypt(self.key, self.key)
        self.assertNotEqual(message1, message3)
        message4 = module.symDecrypt(self.key, self.key)

    def test_symEncryptBase64(self):
        message1 = 'MSG1'
        encrypted_b64 = module.symEncrypt_b64(message1, self.key)
        message2 = module.symDecrypt_b64(encrypted_b64)


if __name__ == '__main__':
    unittest.main()