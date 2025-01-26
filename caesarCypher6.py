alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(original_Text, shift_Amount):
    encoded_string = ""
    for letter in original_Text:
        list_Length = len(alphabet) - 1
        count = alphabet.index(letter)
        # Handle the last letter in the list from the alphabet.
        # Without this, the program would crash with a
        # 'list index out of range' error.
        if count == list_Length:
            count = 0
            count += shift_Amount
            encoded_string = encoded_string + alphabet[count]
        else:
            count = alphabet.index(letter)
            count += shift_Amount
            encoded_string = encoded_string + alphabet[count]

    # The below code is written after the above section.
    # for letter in original_Text:
    #     shifted_Position = alphabet.index(letter) + shift_Amount

    #     shifted_Position %= len(alphabet)  # 0 - 25
    #     encoded_string += alphabet[shifted_Position]

    print(f"Here is the encoded result: {encoded_string}")


# encrypt(original_Text=text, shift_Amount=shift)


def decrypt(original_Text, shift_Amount):
    decoded_string = ""
    for letter in original_Text:
        list_Length = len(alphabet) - 1
        count = alphabet.index(letter)
        # Handle the last letter in the list from the alphabet.
        # Without this, the program would crash with a
        # 'list index out of range' error.
        if count == list_Length:
            count = 0
            count -= shift_Amount
            decoded_string = decoded_string + alphabet[count]
        else:
            count = alphabet.index(letter)
            count -= shift_Amount
            decoded_string = decoded_string + alphabet[count]

    # The below code is written after the above section.
    # for letter in original_Text:
    #     shifted_Position = alphabet.index(letter) - shift_Amount

    #     shifted_Position %= len(alphabet)  # 0 - 25
    #     decoded_string += alphabet[shifted_Position]

    print(f"Here is the decoded result: {decoded_string}")


# decrypt(original_Text=text, shift_Amount=shift)


def caesar(original_Text, shift_Amount, encode_or_decode):
    output_string = ""

    if encode_or_decode == "decode":
        shift_Amount *= -1

    for letter in original_Text:

        if letter not in alphabet:
            output_string += letter
        else:
            shifted_Position = alphabet.index(letter) + shift_Amount
            shifted_Position %= len(alphabet)  # 0 - 25
            output_string += alphabet[shifted_Position]
    print(f"Here is the {encode_or_decode}d result: {output_string}")


should_Continue = True


while should_Continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
    direction.lower()

    text = input("Type your message: \n").lower()

    shift = int(input("Type the shift number: \n"))

    caesar(original_Text=text, shift_Amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. otherwise, type 'no'. \n").lower()

    if restart == "no":
        should_Continue = False
        print("Goodbye!")
    else:
        should_Continue = True
