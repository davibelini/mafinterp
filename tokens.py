from enum import Enum 

class TokenType(Enum):
  NUMBER = 0
  PLUS = 1
  MINUS = 2
  MULTIPLY = 3
  DIVIDE = 4
  LPAR = 6
  RPAR = 5

class Token():
  def __init__(self, type: TokenType, value=None):
     self.type = type
     self.value = value
