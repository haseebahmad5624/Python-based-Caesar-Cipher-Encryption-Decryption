def encrypt(text, shift):
    encrypted = ""

    for char in text:
        if char.isupper():
            encrypted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            encrypted += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted += char

    return encrypted


def decrypt(text, shift):
    decrypted = ""

    for char in text:
        if char.isupper():
            decrypted += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        elif char.islower():
            decrypted += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            decrypted += char

    return decrypted


print("=======================================")
print(" BASIC ENCRYPTION & DECRYPTION SYSTEM ")
print("=======================================")

while True:
    message = input("\nEnter your message: ")
    shift = int(input("Enter shift key: "))

    encrypted_text = encrypt(message, shift)
    decrypted_text = decrypt(encrypted_text, shift)

    print("\nOriginal Message :", message)
    print("Encrypted Message:", encrypted_text)
    print("Decrypted Message:", decrypted_text)

    choice = input("\nDo you want to encrypt another message? (Y/N): ").strip().upper()

    if choice != "Y":
        print("\nThank you for using the Basic Encryption & Decryption System.")
        print("Program Ended Successfully!")
        break