import sys

def encrypt(message, k):
    message = message.lower()
    encrypted_message = ""
    for char in message:
        if char.islower():
            encrypted_message += chr((ord(char) + k - 97) % 26 + 97)
        else:
            encrypted_message += char    
    return encrypted_message

def decrypt(message, k):
    message = message.lower()
    decrypted_message = ""
    for char in message:
        if char.islower():
            decrypted_message += chr((ord(char) - k - 97) % 26 + 97)
        else:
            decrypted_message += char
    return decrypted_message   

if __name__ == "__main__":
    message = "guided intuition"
    key = 4       

encryptedmessage = encrypt(message, 4)
print(encryptedmessage)
decryptedmessage = decrypt(encryptedmessage, 4)
print(decryptedmessage)