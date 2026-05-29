# Day 8: Function with Parameters (Encryption and Decryption)
#========================================
# Explanation of this project:
# This project is a simple function that encrypts and decrypts the user's choices as input and outputs the result.
#========================================

# Encryption and Decryption (Caesar Cipher)
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(orignal_text, shift_amount):
    cipher_text = ""
    for letter in orignal_text:
        if letter in alphabets:
            position = alphabets.index(letter) + shift_amount
            position %= 26 
            new_position = alphabets[position]
            cipher_text += new_position 
        else:
            cipher_text += letter
    return cipher_text
        
print(encrypt(orignal_text=input("Enter the text you want to encode: ").lower(),
        shift_amount=int(input("Enter the shift value: "))))


def decrypt(orignal_text, shift_amount):
    cipher_text = ""
    for letter in orignal_text:
        if letter in alphabets:
            position = alphabets.index(letter) - shift_amount
            position %= len(alphabets) 
            new_position = alphabets[position]
            cipher_text += new_position
        else:
            cipher_text += letter
    print(f"The decrypted text is {cipher_text}")

decrypt(orignal_text=input("Enter the text you want to decrypt: ").lower(),
            shift_amount=int(input("Enter the shift value: ")))


repeat = input("Do you want to go again? (Y for Yes/N for No): ").lower()
while repeat == "y":
    enc_or_dyc = input("Do you want to repeat encrypt or decrypt (E for encrypt/D for decrypt): ").lower()
    if enc_or_dyc == "e":
        encrypt(orignal_text=input("Enter the text you want to encode: ").lower(),
        shift_amount=int(input("Enter the shift value: ")))
    elif enc_or_dyc == "d":
        decrypt(orignal_text=input("Enter the text you want to decrypt: ").lower(),
            shift_amount=int(input("Enter the shift value: ")))
            
    repeat = input("Do you want to go again? (Y for Yes/N for No): ").lower()

print("Thank You for using our encryption and decryption tool")