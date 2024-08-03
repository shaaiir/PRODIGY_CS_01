def caesar_encrypt(plaintext, shift_value):
    """Encrypt the plaintext using Caesar Cipher with a given shift value."""
    encrypted_text = ""
    shift_amount = shift_value % 26  # Normalize the shift value to wrap around the alphabet

    for char in plaintext:
        if char.isalpha():  # Check if the character is an alphabet letter
            if char.islower():
                start = ord('a')  # ASCII code for 'a' to handle lowercase letters
            else:
                start = ord('A')  # ASCII code for 'A' to handle uppercase letters

            # Compute the new character by shifting and wrapping around the alphabet
            encrypted_char = chr(start + (ord(char) - start + shift_amount) % 26)
            encrypted_text += encrypted_char
        else:
            # Non-alphabetic characters are not encrypted
            encrypted_text += char

    return encrypted_text

def caesar_cipher_decrypt(ciphertext, shift_value):
    """Decrypt the ciphertext by reversing the shift."""
    return caesar_encrypt(ciphertext, -shift_value)

def main():
    """Main function to interact with the user for encryption or decryption."""
    print("Welcome to the Caesar Cipher Tool!")
    print("You can encrypt or decrypt a message using the Caesar Cipher.")
    print("Choose an option below:")
    print("1. Encrypt a message")
    print("2. Decrypt a message")

    choice = input("Please enter your choice (1 or 2): ").strip()

    if choice not in ('1', '2'):
        print("Oops! That's not a valid choice. Please enter 1 or 2.")
        return

    message = input("Enter the message you want to process: ")
    shift = int(input("Enter the shift value (an integer): "))

    if choice == '1':
        encrypted_message = caesar_encrypt(message, shift)
        print(f"Here is your encrypted message: {encrypted_message}")
    elif choice == '2':
        decrypted_message = caesar_cipher_decrypt(message, shift)
        print(f"Here is your decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
