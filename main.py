from Diffie_Hellman import *
from Vigenere import *
from Playfair import *

key = DH()
print("_________________________")
msg = input("Enter the message to encrypt: ")

encrypted_message = vigenere(msg,key)
print(f"Vigenere Cipher: Encrypted Message: {encrypted_message}")


encrypted_message = playfair(encrypted_message,key)
print(f"playfair Cipher: Encrypted Message: {encrypted_message}")


