#!/usr/bin/env python

import base64

from Crypto import Random
from Crypto.Cipher import AES

def pad(s):
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

def symEncrypt(message, key):
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(pad(message))

def symDecrypt(cipher_text, key):
    iv = cipher_text[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plain_text = cipher.decrypt(cipher_text[AES.block_size:])
    return plain_text.rstrip(b"\0")

def symEncrypt_b64(message_b64, key_b64):
    message = base64.b64decode(message_b64)
    key = base64.b64decode(key_b64)
    return base64.b64encode(symEncrypt(message, key))

def symDecrypt_b64(cipher_b64, key_b64):
    cipher_bin = base64.b64decode(cipher_b64)
    key = base64.b64decode(key_b64)
    return symDecrypt(cipher_bin, key)