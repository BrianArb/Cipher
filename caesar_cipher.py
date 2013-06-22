#!/usr/bin/env python

"""Caesar cipher class.
In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift
cipher, Caesar's code or Caesar shift, is one of the simplest and most
widely known encryption techniques.
It is a type of substitution cipher in which each letter in the plaintext
is replaced by a letter some fixed number of positions down the alphabet.
For example, with a left shift of 3, D would be replaced by A, E would
become B, and so on.
The method is named after Julius Caesar, who used it in his
private correspondence.
"""

class CaesarCipher(object):
  """Caesar cipher, is one of the simplest encryption techniques."""
  
  cipher = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

  def __init__(self, message, shift_by=3):
    """Constructor for CaesarCipher.

    Args:
      message: the message to encrypted or decryted.
      shift_by: the number to offset by [1, 25].
    """
    self.message = [character.upper() for character in message]
    self.shift_by = shift_by % 26

  def encrypt(self):
    """Encrypt string using cipher.
    The encryption can also be represented using modular arithmetic by first
    transforming the letters into numbers, according to the scheme,
    A = 0, B = 1,..., Z = 25.
    Encryption of a letter by a shift n can be described mathematically as...

    En(X) = (x + n) mod 26

    Returns:
      string: The encrypted string.
    """
    encrypted_string = ''
    for character in self.message:
      if character in self.cipher:
        encrypt_index = (self.cipher.index(character) + self.shift_by) % 26
        encrypted_string += self.cipher[encrypt_index]
      else:
        encrypted_string += character

    return encrypted_string

  def decrypt(self):
    """Decrypt string using cipher.
    
    Decryption is performed similarly to the encryption scheme.
    Decryption of a letter by a shift n can be described mathematically as...

    Dn(X) = (x - n) mod 26

    Returns:
      string: The decrypted string.
    """
    decrypted_string = ''
    for character in self.message:
      if character in self.cipher:
        decrypt_index = (self.cipher.index(character) - self.shift_by) % 26
        decrypted_string += self.cipher[decrypt_index]
      else:
        decrypted_string += character

    return decrypted_string

