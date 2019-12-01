#!/usr/bin/python

import unittest
from maths import Number

class MathTests(unittest.TestCase):
  def test_constructor_assigns_value(self):
    num = 4
    numberInstance = Number(num)
    self.assertEqual(num,numberInstance.value)

  def test_absolute_positive(self):
    num = 3
    numberInstance = Number(num)
    self.assertGreater(numberInstance.absolute(),0)

  def test_absolute_negative(self):
    num = -3
    numberInstance = Number(num)
    self.assertGreater(numberInstance.absolute(), 0)

  def test_absolute_zero(self):
    num = 0
    numberInstance= Number(num)
    self.assertEqual(numberInstance.absolute(), 0)