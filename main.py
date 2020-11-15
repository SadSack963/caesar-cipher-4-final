alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    shift = shift % 26

    if direction == "decode":
        shift = 26 - shift
    elif direction != "encode":
        print("You must type either ENCODE or DECODE")
        return

    output = ""

    for x in text:
        if x in alphabet:
            output += alphabet[(alphabet.index(x) + shift) % 26]
        else:
            output += x

    print(f"The {direction}d text is \n{output}\n")

import art
print(art.logo)

restart = True
while restart:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar(text=text, shift=shift, direction=direction)

    again = input("Do you want to continue? (Yes)/No : ").lower()
    if again == "no":
        print("Goodbye")
        restart = False
