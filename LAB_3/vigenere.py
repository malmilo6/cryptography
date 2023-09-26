
# Shift matrix rows
def shift_row(input_string, n):
    n = n % len(input_string)
    return input_string[n:] + input_string[:n]


# Create matrix
def create_matrix(alphabet):
    matrix = []
    for i in range(0, len(alphabet)):
        matrix.append([shift_row(alphabet, i)])

    return matrix


# Extend the key to the length of enc string
def create_key(string, key):
    a, b = divmod(len(string), len(key))
    new_key = a * key + key[:b]
    return new_key


# Create array of indexes
def create_indexes(alphabet, string):
    string_of_indexes = []
    for char in string:
        string_of_indexes.append(alphabet.index(char))

    return string_of_indexes


# Input validation
def validation(string, alphabet):
    string = string.upper()
    for char in string:
        if char in alphabet:
            pass
        else:
            return False
    return True


# Cipher
def vigenere_cipher(alphabet, key, string, operation):
    if validation(key, alphabet) and validation(string, alphabet):
        key = key.replace(' ', '').upper()
        string = string.replace(' ', '').upper()

        matrix = create_matrix(alphabet)
        key = create_key(string, key)
        key_indexes = create_indexes(alphabet, key)
        string_indexes = create_indexes(alphabet, string)

        if operation == 'encrypt':
            encrypted_word = ''
            for k, v in zip(key_indexes, string_indexes):
                encrypted_word += matrix[k][0][v]
            return f'Encrypted message is {encrypted_word}.'
        else:
            decrypted_word = ''
            for k, v in zip(key_indexes, string_indexes):
                _, m = divmod((v-k), 26)
                decrypted_word += alphabet[m]

            return f'Decrypted message is {decrypted_word}.'
    else:
        print('The input contains the character that is not allowed. Please use only the letters '
              'only from romanian alphabet')
        return


if __name__ == '__main__':
    alphabet_eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_ro = 'AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ'

    key = 'SUPER'
    string_to_enc = 'PERASPERAADASTRA'
    string_to_dec = 'HYGEJHYGERVUHXIS'
    operations = ['encrypt', 'decrypt']
    print(vigenere_cipher(alphabet_ro, key, string_to_dec, operations[1]))
