text = input("Enter your text: ")
key = int(input("Enter your key: "))
choice = int(input("Press '1' to encrypt or '2' to decrypt: "))

def encrypt(text, key):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + key - 65) % 26 + 65)
        else:
            result += chr((ord(char) + key - 97) % 26 + 97)
    return result

def decrypt(text, key):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) - key - 65) % 26 + 65)
        else:
            result += chr((ord(char) - key - 97) % 26 + 97)
    return result

result = ''

if choice == 1:
    result = encrypt(text, key)
elif choice == 2:
    result = decrypt(text, key)
else:
    print("Invalid choice")
    exit()
    
print("Result: ", result)