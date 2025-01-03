from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import base64
import os

def get_key_iv() -> tuple:
    with open("bin/key.bin", "rb") as key_file:
        key = key_file.read()
    with open("bin/iv.bin", "rb") as iv_file:
        iv = iv_file.read()
    return (key, iv)

def encrypt(data: bytes) -> bytes:
    # 创建加密器实例
    backend = default_backend()
    key, iv = get_key_iv()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()

    # 填充数据以满足AES块大小要求
    padded_data = padder.update(data) + padder.finalize()
    # 加密数据
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    return encrypted_data

def decrypt(data: bytes) -> bytes:
    # 创建解密器实例
    backend = default_backend()
    key, iv = get_key_iv()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()
    unpadder = padding.PKCS7(128).unpadder()

    # 解密数据
    decrypted_padded_data = decryptor.update(data) + decryptor.finalize()

    # 移除填充
    decrypted_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()

    return decrypted_data
