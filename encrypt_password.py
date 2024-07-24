import os
import rsa

if not (os.path.exists("rsa_keys/publicKey.pem") and os.path.exists("rsa_keys/privateKey.pem")):
    publicKey, privateKey = rsa.newkeys(2048)
    with open("rsa_keys/publicKey.pem", "wb") as key:
        key.write(publicKey.save_pkcs1("PEM"))

    with open("rsa_keys/privateKey.pem", "wb") as p_key:
        p_key.write(privateKey.save_pkcs1("PEM"))

else:
    with open("rsa_keys/publicKey.pem", "rb") as p:
        publicKey = rsa.PublicKey.load_pkcs1(p.read())

    with open("rsa_keys/privateKey.pem", "rb") as p:
        privateKey = rsa.PrivateKey.load_pkcs1(p.read())


def encrypt_pass(un_enc_password):
    enc_password = rsa.encrypt(un_enc_password.encode(), publicKey)
    return enc_password


def decrypt_pass(enc_password):
    dec_message = rsa.decrypt(enc_password, privateKey).decode()
    return dec_message
