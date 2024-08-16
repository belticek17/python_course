letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
           ]


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == 'decode':
        shift_amount *= -1

    for char in original_text:
        if char not in letters:
            output_text += char

        else:
            shifted_position = letters.index(char) + shift_amount
            shifted_position %= len(letters)
            output_text += letters[shifted_position]

    print(f"Here is the {encode_or_decode}d result: {output_text} and the shift_amount is: {shift_amount}")


def main():
    can_continue = True
    while can_continue:
        function = input("Type 'encode' to encrypt a message, type 'decode' to decode the message!\n")
        text = input('Type your message:\n').lower()
        shift = int(input("Type the shift number:\n"))
        caesar(original_text=text, shift_amount=shift, encode_or_decode=function)

        restart = input("Type 'yes' if you want to continue. Otherwise type 'no'!\n").lower()

        if restart == 'no':
            can_continue = False
            print("Goodbye!")


if __name__ == '__main__':
    main()
