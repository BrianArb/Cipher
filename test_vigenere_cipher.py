#!/usr/bin/env python

import unittest

from vigenere_cipher import VigenereCipher

PLAINTEXT = 'ATTACK AT DAWN'
KEY = 'LEMON'
CIPHERTEXT = 'LXFOPV EF RNHR'

class TestEncryptString(unittest.TestCase):
  
  def setUp(self):
    self.msg = VigenereCipher(KEY, PLAINTEXT)
  
  def test_isinstance(self):
    self.assertIsInstance(self.msg, VigenereCipher)
  
  def test_isequals(self):
    check = self.msg.encrypt()
    expect = CIPHERTEXT
    self.assertEquals(check, expect)


class TestDecryptString(unittest.TestCase):
  
  def setUp(self):
    self.msg = VigenereCipher(KEY, CIPHERTEXT)
  
  def test_isinstance(self):
    self.assertIsInstance(self.msg, VigenereCipher)
  
  def test_isequals(self):
    check = self.msg.decrypt()
    expect = PLAINTEXT
    self.assertEquals(check, expect)
  

if __name__ == '__main__':
  unittest.main()