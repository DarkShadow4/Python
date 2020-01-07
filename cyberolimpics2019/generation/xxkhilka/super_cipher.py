#!/usr/bin/python3

from random import randrange
from math import sqrt
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Util.number import *
import time
import gmpy2
import sys

class SuperCipher: 
    def __init__(self): 
        pass
    def generate_RSA(self): 
        d = -1
        while d < 0:
            p = 28277272362593115574162224052619470725038628666889601331597105112170509643981266853694602855529366909474562278005327834733737755215681368934735735832862478471228814943268281536498643898775692118710673320037247359796839778461664626242782222021380594353008388638115773763101632371701976567360308579291564965699318713570413315108362492873099207171799547065211013972090450001057029746332549121729370479079695429599013550127567344899046866362325123662470876455909156389181407806004162642643940158409858858116044387921366649528694401269686222693002337381450641778254726313655196246487215134360927843149101559041683523165493
            q = self.getmillis()
            print("Will generate Q with " + str(q) + " milliseconds")
            while not isPrime(q): 
                q+=1

            n = p * q
            i_Euler = (p-1) * (q-1)
            e = 65537
            try:
                d = int(gmpy2.invert(e, i_Euler))
            except ZeroDivisionError: 
                continue

        new_key = RSA.construct([n, e, d])
        public_key = new_key.publickey().exportKey("PEM")
        private_key = new_key.exportKey("PEM")

        return public_key, private_key

    def getmillis(self): 
        return int(round(time.time()*1000))

    def encrypt(self, input_file, public, output_file): 
        file_in = open(input_file, "rb")
        data = file_in.read()
        file_in.close()

        recipient_key = RSA.importKey(public)
        session_key = get_random_bytes(16)

        # Encrypt the session key with the public RSA key
        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        enc_session_key = cipher_rsa.encrypt(session_key)

        # Encrypt the data with the AES session key
        cipher_aes = AES.new(session_key, AES.MODE_ECB)
        ciphertext = cipher_aes.encrypt(self.pad(data))

        file_out = open(output_file, "wb")
        [file_out.write(x) for x in (enc_session_key, ciphertext)]
        file_out.close()

        return ciphertext

    def pad(self, data): 
        length = 16 - (len(data) % 16)
        data += bytes([length])*length
        return data

    def decrypt(self, input_file, private, output_file): 
        file_in = open(input_file, "rb")
        private_key = RSA.importKey(private)
        enc_session_key, ciphertext = \
            [ file_in.read(x) for x in (int(private_key.size()/8+1), -1) ]
        file_in.close()

        # Decrypt the session key with the private RSA key
        cipher_rsa = PKCS1_OAEP.new(private_key)
        session_key = cipher_rsa.decrypt(enc_session_key)

        # Decrypt the data with the AES session key
        cipher_aes = AES.new(session_key, AES.MODE_ECB)
        data = cipher_aes.decrypt(ciphertext)
        
        file_out = open(output_file, "wb")
        file_out.write(data)
        file_out.close()

        return data
