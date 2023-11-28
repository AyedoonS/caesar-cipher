"""
CAESAR CIPHER

A Caesar Cipher encryption function, which is "a simple encryption
technique that involves shifting the characters of a string by a
fixed number of positions given by int <key>." Characters are 'wrapped'
if needed.
    * If key > 1, characters are shifted <key> forward
        - (i.e. if key = 1, a -> b, or z -> a)
    * If key < 1, characters are shifted <key> backward
        - (i.e., if key = -1,  b -> a, or a -> z)
    * If key = 0, nothing is shifted

Encrypts .txt files
"""

def caesar_cipher_helper(sentence: list[list[str]],
                         key: int) -> list[list[str]]:
    """
    Caesar Cipher encrypt/decrypt helper function:

    Shifts characters of sentence: list[list[str] <key> forward if key > 0,
    or <key> backward  if key < 0. Characters are not shifted if <key> = 0
    (so to decrypt a file, <key> needs to be [-1 * <o_key>] where <o_key> was
    the key originally used to encrypt it...)
    """
    for lines in range(len(sentence)):
        for words in range(len(sentence[lines])):

            acc = ''    # <- accumulator string
            for ch in sentence[lines][words]:
                if ch.isalpha() and ch.isupper():   # <- uppercase letters
                    ch = chr(((ord(ch) - ord('A') + key) % 26) + ord('A'))
                elif ch.isalpha() and ch.islower():  # <- lowercase letters
                    ch = chr(((ord(ch) - ord('a') + key) % 26) + ord('a'))
                acc += ch
            sentence[lines][words] = acc
    return sentence


def caesar_cipher_encrypt(source_file: str,
                          encrypted_file: str, key: int) -> None:
    """
    Encrypts contents of <source_file> into <encrypted_file>
    """
    try:
        file_lines = []
        with open(source_file, 'r') as read_file:
            for lines in read_file:
                file_lines.append(lines.split())
            file_lines = caesar_cipher_helper(file_lines, key)

        with open(encrypted_file, 'w+') as write_file:
            for lines in file_lines:
                for word in lines:
                    write_file.write(word + ' ')
                write_file.write('\n')

    except FileNotFoundError as err1:
        print('One or more files or directories could not be found')
    return None
