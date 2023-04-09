alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def shift_alphabet(number):
    global alpha
    new_alpha = alpha[number:]
    new_alpha += alpha[:number]
    return new_alpha

def request_message():
    return input('Type your message: ')

def request_shiftnum():
    shiftnum = input('Type the shift number: ')
    if shiftnum.isnumeric():
        return int(shiftnum) % 26
    request_shiftnum()
        
def cipher(mode):
    message = request_message()
    shift_num = request_shiftnum()
    if mode == 'decode':
        shift_num *= -1
    ciphered_message = ''
    global alpha
    encoded_alpha = shift_alphabet(shift_num)
    for char in message:
        if char.isalpha():
            position = alpha.index(char.lower())
            ciphered_message += encoded_alpha[position]
        else:
            ciphered_message += char
    print(f"\nHere's the {mode}d message: {ciphered_message}")


if __name__ == '__main__':
    active = 'y'

    while active[0].lower() == 'y':
        cipher_method = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
        if cipher_method.lower() in ['encode','decode']:
            cipher(cipher_method)
        else:
            print("Only 'encode' and 'decode' are accepted." )
        active = input("Type 'yes' if you want to go again. Other wise type 'no'. ")