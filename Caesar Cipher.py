from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

stop=False
while stop==False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def encrypt(original_text, shift_amount):
        cipher_text = ""
        for letter in original_text:
            if letter in alphabet:
                shifted_position = alphabet.index(letter) + shift_amount
                shifted_position %= len(alphabet)
                cipher_text += alphabet[shifted_position]
            else:
                cipher_text+=letter
        print(f"Here is the encoded result: {cipher_text}")
    def decrypt(text,shit):
        cipher=""
        for letter in text :
            if letter in text:
                x=alphabet.index(letter)
                y=x-shift
                cipher += alphabet[y]
            else:
                cipher+=letter
        print(f"Here is the message after the decoding {cipher}")

    if direction=="encode":
        encrypt(original_text=text, shift_amount=shift)
    elif direction=="decode":
        decrypt(text, shift)
    else :
        print("Invalid input try again")
    stop_game=input("Would you like to continue the type ' game yes / no' ")

    if stop_game.lower()=="yes":
        stop=False
    elif stop_game.lower()=="no":
        stop=True
    else:
        print("Invalid input")
        stop=False




