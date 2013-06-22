#!/usr/bin/env python

"""The Vigenere cipher is a method of encrypting alphabetic text by using a
   series of different Caesar ciphers based on the letters of a keyword.
   It is a simple form of polyalphabetic substitution.

   referances:
    http://en.wikipedia.org/wiki/Vigenere_cipher
"""


LETTERS = [chr(number) for number in xrange(65, 65 + 26)]


class VigenereCipher(object):
  """The Vigenere cipher object.

  Attributes:
    key: string used as key to encrypt and decrypt text.
    message: string to encrypt or decrypt.
  """

  def __init__(self, key, message=None):
    self.key = key
    self.message = message.upper()

  def encrypt(self):
    """Encryt the text using the Vigenere Cipher.

    Vigenere can also be viewed algebraically. If the letters A Z are taken
    to be the numbers 0 25, and addition is performed modulo 26, then
    Vigenere encryption using the key can be written...

    Ci = Ek(Mi) = (Mi + Ki) mod 26
    Thus using the previous example, to encrypt A=0  with key letter L=11
    the calculation would result in 11=L.
    11 = (0 + 11) mod 26

    Returns:
      string: encrypted string
    """

    encrypted_string = ''
    key_lenght = len(self.key)
    key_index = 0
    for character in self.message:
      if character in LETTERS:
        index_of_character = LETTERS.index(character)
        key_character = self.key[key_index % key_lenght]
        index_of_key = LETTERS.index(key_character)
        index_of_encrypted_character = (index_of_character + index_of_key) % 26
        character = LETTERS[index_of_encrypted_character]
        key_index += 1

      encrypted_string += character

    return encrypted_string

  def decrypt(self):
    """Decryt the text using the Vigenere Cipher.

    Vigenere can also be viewed algebraically. If the letters A Z are taken
    to be the numbers 0 25, and addition is performed modulo 26, then
    Vigenere encryption using the key can be written...

    Mi = Dk(Ci) = (Ci + Ki) mod 26
    Thus using the previous example, to decrypt R=17  with key letter E=4
    the calculation would result in 13=N.
    13 = (17 + 4) mod 26

    Returns:
      string: decrypted string
    """

    decrypted_string = ''
    key_lenght = len(self.key)
    key_index = 0
    for character in self.message:
      if character in LETTERS:
        index_of_character = LETTERS.index(character)
        key_character = self.key[key_index % key_lenght]
        index_of_key = LETTERS.index(key_character)
        index_of_decrypted_character = (index_of_character - index_of_key) % 26
        character = LETTERS[index_of_decrypted_character]
        key_index += 1

      decrypted_string += character

    return decrypted_string
