from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import base64
import os

def gen_key():
    key = os.urandom(32)
    return key

def gen_iv():
    iv = os.urandom(16)
    return iv

def save_key_iv(key, iv):
    # 保存密钥和IV，以便以后解密
    with open('key.bin', 'wb') as key_file:
        key_file.write(key)

    with open('iv.bin', 'wb') as iv_file:
        iv_file.write(iv)

save_key_iv(gen_key(),gen_iv())
