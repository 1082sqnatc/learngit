#!/usr/bin/python

class Number:
  """
  Math function library wrapping basic types with a Number class
  
  Attributes
  ----------
  value: number
    The initial value of this Number. Is never mutated.
  
  Methods
  -------
  add(other: number): Number
    Returns a new Number instance with the value of self.value plus
    the new other number value added to it.
  """
  
  def __init__(self, value):
    """
    Parameters
    ----------
    value: number
      The initial value of this instance
    """

    self.value = value

  def add(self,other):
    """
    Returns a new Number instance with self.value + other: number as the value
    
    Parameters
    ----------
    other: number
      The other basic instrinsic number value to add to self.value
    """

    #return new Number(self.value + second)
    return self.value + other

  def absolute(self):
    if self.value > 0:
      return self.value
    else:
      return -1 * self.value
