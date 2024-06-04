#!/usr/bin/env python3

class MyString:
  def __init__(self, value=''):
    if isinstance(value, str):
      self._value = value
    else:
      print("The value must be a string.")

  @property
  def value(self):
    return self._value

  @value.setter
  def value(self, new_value):
    if isinstance(new_value, str):
      self._value = new_value
    else:
      print("The value must be a string.")

  def is_sentence(self):
    if self._value[-1] == '.':
      return True
    else: 
      return False
    
  def is_question(self):
    if self._value[-1] == '?':
      return True
    else: 
      return False
    
  def is_exclamation(self):
    if self._value[-1] == '!':
      return True
    else: 
      return False
    
  def count_sentences(self):
    count = 0
    for letter in self._value:
      if letter == '.' or letter == '?' or letter == '!':
        count += 1
    return count



      
