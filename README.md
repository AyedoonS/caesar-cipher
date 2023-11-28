# caesar-cipher
A very basic caesar-cipher encryption algorithm in Python3 involving File I/O.

The function takes in three parameters: 
- str: source_file (i.e., "read file" - the file whose contents are to be encrypted)
- str: encrypted_file (i.e., "write file" - the file where encrypted text is to be written)
- int: key (the character shift for the algorithm)

If a separate write file is not needed, directly write to read file in the function parameter.
(in other words, set source_file = encrypted_file.

To decrypt an encrypted file, key must equal the negative of the key used to encrypt the file
