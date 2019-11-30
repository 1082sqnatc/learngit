#!/usr/bin/python

import unittest
from maths import Number

class MathTests(unittest.TestCase):
  def test_constructor_assigns_value(self):
    num = 4
    numberInstance = Number(num)
    self.assertEqual(num,numberInstance.value)

