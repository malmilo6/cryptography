def caesar_cipher(text, shift, operation, alphabet):
    text = text.upper()
    text = text.replace(' ', '')
    encrypted_text = ""
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            if operation == "encrypt":
                new_index = (index + shift) % 26
            else:
                new_index = (index - shift) % 26
            encrypted_text += alphabet[new_index]
        else:
            print(f"The character '{char}' is not allowed. Please use only the letters 'A'-'Z' or 'a'-'z'.")
            return

    return encrypted_text


def caesar_cipher_extended(text, shift, key, operation, alphabet):
    key = remove_duplicates(key)
    modified_alphabet = rotate_left(remove_duplicates((key + alphabet).upper()), shift)

    return caesar_cipher(text, shift, operation, modified_alphabet)


def remove_duplicates(input_string):
    output_string = ""
    for char in input_string:
        if char not in output_string:
            output_string += char
    return output_string


# Apply the shift to the obtained alphabet
def rotate_left(input_string, n):
    n = n % len(input_string)
    return input_string[n:] + input_string[:n]


# Test cases
if __name__ == "__main__":
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    operations = ['encrypt', 'decrypt']
    enc_mess = 'masd'
    dec_mess = 'QBVF'
    key = 'cryptography'
    print(caesar_cipher_extended(dec_mess, 2, key, operations[1], alphabet))

