
# method to Encrypt using Vigenere cipher takes the msg and key as argument and return the cipher text
def vigenere(msg, key):
    cipher_text= ''
    
    # Extend the key to match the length of the message
    key_repeated = (key * (len(msg) // len(key))) + key[:len(msg) % len(key)]
    
    # loop through each character in the message.
    for i in range(len(msg)):
        # Calculate the shift based on the corresponding character in the repeated key.
        shift = ord(key_repeated[i].upper()) - ord('A')
        
        # Encrypt uppercase letters.
        if msg[i].isupper():
            cipher_text += chr((ord(msg[i]) + shift - ord('A')) % 26 + ord('A'))
        # Encrypt lowercase letters.
        elif msg[i].islower():
            cipher_text += chr((ord (msg[i]) + shift - ord('a')) % 26 + ord('a'))
        # If the character is neither, just add it as is.
        else:
            cipher_text += msg[i]
    
    # Return the encrypted cipher text.
    return cipher_text
