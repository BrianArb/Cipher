#!/usr/bin/env python

import string
import unittest

from caesar_cipher import CaesarCipher

SHIFT_BY = 23
PLAIN =  'the quick brown fox jumps over the lazy dog'
CIPHER = 'QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD'

class TestEncryptString(unittest.TestCase):
  
  def setUp(self):
    self.message = CaesarCipher(PLAIN, SHIFT_BY)
  
  def test_isinstance(self):
    self.assertIsInstance(self.message, CaesarCipher)
  
  def test_encrypt(self):
    check = self.message.encrypt()
    expect = CIPHER
    self.assertEquals(check, expect)

class TestDecryptString(unittest.TestCase):
  
  def setUp(self):
    self.message = CaesarCipher(CIPHER, SHIFT_BY)
  
  def test_isinstance(self):
    self.assertIsInstance(self.message, CaesarCipher)
  
  def test_decrypt(self):
    check = self.message.decrypt()
    expect = PLAIN.upper()
    self.assertEquals(check, expect)


if __name__ == '__main__':
  unittest.main()
