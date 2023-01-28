# Theodoro Bertol Dev (Abeelha) #
# || Day 8 of #100DaysOfCode || #

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
correct_input = False

def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        cipher_text += alphabet[new_position]
  print(f"The encoded text is {cipher_text}")

#TODO-1 CHECK: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

def decrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        cipher_text += alphabet[new_position]
    print(f"The decoded text is {cipher_text}")

  #TODO-2 CHECK: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3 CHECK: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

while not correct_input:
    if direction == "encode":
        correct_input = True
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encrypt(plain_text=text, shift_amount=shift)
    elif direction == "decode":
        correct_input = True
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        decrypt(plain_text=text, shift_amount=shift)
    else:
        print("You didnt inform correctly 'encode' or 'decode', try again:\n")
    

