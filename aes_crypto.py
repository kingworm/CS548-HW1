# -*- coding: utf-8 -*-
import crypto 
import sys
sys.modules['Crypto'] = crypto
from Crypto import Random
from Crypto.Cipher import AES

BLOCK_SIZE=16

class AESCryptoCBC():
    def __init__(self, key):
        #Initial vector를 0으로 초기화하여 16바이트 할당함
        iv = chr(0) * 16
        # aes cbc 생성
        self.crypto = AES.new(key, AES.MODE_CBC, iv)

    def encrypt(self, data):
        #암호화 message는 16의 배수여야 한다.
        enc = self.crypto.encrypt(data)
        return enc

    def decrypt(self, enc):
        #복호화 enc는 16의 배수여야 한다.
        dec = self.crypto.decrypt(enc)
        return dec

#키 32바이트 = aes 256
key = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

#원본 데이터
data1 = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
data2 = [0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
data3 = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01]

#출력
# print("Data 1 is " + str(data1))
# print("Data 2 is " + str(data2))
# print("Data 3 is " + str(data3))

#키 생성
aes = AESCryptoCBC(bytes(key))
#변경
enc1 = aes.encrypt(bytes(data1))
enc2 = aes.encrypt(bytes(data2))
enc3 = aes.encrypt(bytes(data3))

print("problem#1           " , enc1.hex())
print("problem#2 first bit " , enc2.hex())
print("problem#2 last bit  " , enc3.hex())

# print("The encrypted value is " + str(list(enc1)))
# print("The encrypted value is " + str(list(enc2)))
# print("The encrypted value is " + str(list(enc3)))

#키 생성
aes2 = AESCryptoCBC(bytes(key))
#변경
dec1 = aes2.decrypt(bytes(enc1))
dec2 = aes2.decrypt(bytes(enc2))
dec3 = aes2.decrypt(bytes(enc3))
# print("The decrypted value is " + str(list(dec1)))
# print("The decrypted value is " + str(list(dec2)))
# print("The decrypted value is " + str(list(dec3)))

