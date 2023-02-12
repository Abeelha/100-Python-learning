# Theodoro Bertol Dev (Abeelha) #
# || Day 8 of #100DaysOfCode || #

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

#Short code Below
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
      shift_amount *= -1
  for letter in start_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    end_text += alphabet[new_position]
  print(f"Here's the {direction}d result: {end_text}")


#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

#Long code Below:
# correct_input = False
# def caesar(plain_text, shift_amount, direction_choose):
#     cipher_text = ""
#     if direction_choose == "encode":
#         for letter in plain_text:
#             position = alphabet.index(letter)
#             new_position = position + shift_amount
#             cipher_text += alphabet[new_position]
#         print(f"The encoded text is {cipher_text}")
#     if direction_choose == "decode":
#         for letter in plain_text:
#             position = alphabet.index(letter)
#             new_position = position - shift_amount
#             cipher_text += alphabet[new_position]
#         print(f"The decoded text is {cipher_text}")

# while not correct_input:
#     if direction == "encode":
#         correct_input = True
#         text = input("Type your message:\n").lower()
#         shift = int(input("Type the shift number:\n"))
#         caesar(direction_choose = direction, plain_text = text, shift_amount = shift)
#     elif direction == "decode":
#            correct_input = True
#            text = input("Type your message:\n").lower()
#            shift = int(input("Type the shift number:\n"))
#            caesar(direction_choose = direction, plain_text = text, shift_amount = shift)
#     else:
#         print("You didnt inform correctly 'encode' or 'decode', try again:\n")



