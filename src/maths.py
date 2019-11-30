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
  
  __init__(self, value):
    """
    Parameters
    ----------
    value: number
      The initial value of this instance
    """

    self.value = value

  def add(other):
    """
    Returns a new Number instance with self.value + other: number as the value
    
    Parameters
    ----------
    other: number
      The other basic instrinsic number value to add to self.value
    """

    #return new Number(self.value + second)
    return self.value + other


