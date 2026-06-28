# pyperclip because I wanted the clipboard function, cuz its cool
import pyperclip

# simple list including space and numbers hence the word 'alphanumeric'
alphanumerical_list = [' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
length_of_list = len(alphanumerical_list)

# Encryption looks through the list to find the letter then offsets by the shifts and then finds the new character and adds it to the new text variable
def encrypt(text, shifts):
    new_text =""
    for letter_index in range(len(text)):
        temp_shifts = shifts
        for list_index in range(length_of_list):
            if text[letter_index] == alphanumerical_list[list_index]:
                if list_index +shifts>=length_of_list:
                    shifts = shifts - (length_of_list - list_index)
                    list_index=0
                new_char = alphanumerical_list[list_index+shifts]
                new_text += new_char
                shifts = temp_shifts
    return new_text

# Decryption which is similar to encryption looks through the list to find the index of each letter and then offsets the index by the shifts value and then finds that letter and merges it into the new text variable
def decrypt(text, shifts):
    new_text = ""
    for letter_index in range(len(text)):
        temp_shifts = shifts
        for list_index in range(length_of_list):
            if list_index-shifts<0:
                shifts = shifts - length_of_list - list_index
            if text[letter_index] == alphanumerical_list[list_index]:
                new_char = alphanumerical_list[list_index - shifts]
                new_text += new_char
            shifts = temp_shifts
    return new_text

# Main menu basically, also cool text art cuz why not ¯\(o_o)/¯
def main():
    print(" ███   ███  █████  ████  ███  ████      ███  ███ ████  █   █ █████ ████    ")
    print("█ ░░░ █ ░░█ █░░░░░█ ░░░░█ ░░█ █░░░█    █ ░░░  █░░█░░░█ █░  █░█░░░░░█░░░█   ")
    print("█░ ░░░█████░████░░░███░░█████░████░░   █░ ░░░ █░░████░░█████░████░░████░░  ")
    print("█░░   █░░░█░█░░░░   ░░█ █░░░█░█░░█░ ░  █░░    █░░█░░░░ █░░░█░█░░░░ █░░█░ ░ ")
    print(" ███  █░░░█░█████░████░░█░░░█░█░░░█░    ███  ███░█░░░░░█░░░█░█████░█░░░█░  ")
    print(" ░░░  ░░  ░░░░░░░ ░░░░ ░░░  ░░░░  ░     ░░░  ░░░ ░░    ░░  ░░░░░░░ ░░  ░  ")
    print("   ░░░  ░   ░ ░░░░░ ░░░░  ░   ░ ░   ░     ░░░  ░░░ ░     ░   ░ ░░░░░ ░   ░ ")
    while True:
        choice = 4
        try:
            choice = int(input("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
                               "Input 1 for Encryption, Input 2 for Decryption, Input 3 to exit~: "))
        except ValueError:
            print("Please enter a number!!!!!!!!!")
            break
        finally:
            print("Ok!")
        if choice == 1:
            text=input("Enter your text in english only~: ")
            shifts=int(input("Enter the number of shifts~: "))
            cipher_text=encrypt(text, shifts)
            print(f"{cipher_text}, is your encrypted text!!!!")
            pyperclip.copy(cipher_text)
            print("Copied to clipboard!!!")
        elif choice == 2:
            text=input("Enter your ciphertext~: ")
            shifts=int(input("Enter the key (number of shifts)~: "))
            raw_text=decrypt(text, shifts)
            print(f"{raw_text}, is your decrypted text!!!!")
            pyperclip.copy(raw_text)
            print("Copied to clipboard!!!")
        elif choice == 3:
            break
        else:
            print("Please enter 1, 2 or 3!!!!!!!!!")

# modular so that you can import them into other projects :)
if __name__ == "__main__":
    main()