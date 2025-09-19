def encrypt(message, shift):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    new_message=""
    for i in range(len(message)):
        if(message[i]) in alphabet:
            index = alphabet.index(message[i])
            new_index = int(index) + int(shift)
            if(new_index>25):
                new_index = new_index - 26
            new_letter = alphabet[new_index]
            new_message = new_message + new_letter    
        else:
            new_message = new_message + message[i]    
    print(new_message)

def decrypt(message, shift):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    new_message=""
    for i in range(len(message)):
        if(message[i]) in alphabet:
            index = alphabet.index(message[i])
            new_index = int(index) - int(shift)
            if(new_index<0):
                new_index = new_index + 26
            new_letter = alphabet[new_index]
            new_message = new_message + new_letter    
        else:
            new_message = new_message + message[i]    
    print(new_message)

option = input("Write encode to encrypt or decode to decrypt: ")
message = input("Type your message: ")
message = message.lower()
shift = input("Type the shift number: ")
if(option == "encode"):
    encrypt(message,shift)
elif(option == "decode"):
    decrypt(message,shift)
else:
    print("Write encode or decode correctly to use this code")
