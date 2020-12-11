from tokens  import Token, TokenType

class Lexer():
  def __init__(self, text):
    self.text = iter(text) # Don't know what iter does
    self.advance()
  def advance(self):
    try:
      self.current_char = next(self.text)
    except StopIteration:
      self.current_char = None
  def make_token(self):
    while self.current_char != None:
      if self.current_char in " \t\n":
        self.advance()
      elif self.current_char == '.' or self.current_char in "0123456789":
        yield self.make_number()
      elif self.current_char == "+":
        self.advance()
        yield Token(TokenType.PLUS)
      elif self.current_char == "-":
        self.advance()
        yield Token(TokenType.MINUS)
      elif self.current_char == '/':
        self.advance()
        yield Token(TokenType.DIVIDE)
      elif self.current_char == "*":
        self.advance()
        yield Token(TokenType.MULTIPLY)
      elif self.current_char == "(":
        self.advance()
        yield Token(TokenType.LPAR)
      elif self.current_char == ")":
        self.advance()
        yield Token(TokenType.RPAR)
      else:
        print(f"Did not understand unknown char '{self.current_char}'")
        break
  def make_number(self):
    decimal_point_count = 0
    number_str = self.current_char
    self.advance()

    while self.current_char != None and (self.current_char == '.' or self.current_char in "0123456789"):
      if current_char == '.':
        decimal_point_count += 1
        if decimal_point_count > 1:
          break

      number_str += self.current_char
      self.advance()

    if number_str.startswith('.'):
      number_str = '0' + number_str
    if number_str.endswith('.'):
      number_str = number_str + '0'


    return Token(TokenType.NUMBER, float(number_str))