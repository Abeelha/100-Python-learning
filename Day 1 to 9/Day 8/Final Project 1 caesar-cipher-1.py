# Theodoro Bertol Dev (Abeelha) #
# || Day 8 of #100DaysOfCode || #

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
    encrypted_text = ""
    for letter in text:
        index = alphabet.index(letter)
        shifted_index = (index + shift) % 26
        shifted_letter = alphabet[shifted_index]
        encrypted_text += shifted_letter
    print(f"The encoded text is {encrypted_text}")
    

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
input_text = input("Type your message:\n").lower()
input_shift = int(input("Type the shift number:\n"))
encrypt(text = input_text, shift = input_shift)