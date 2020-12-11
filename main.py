from lexer import Lexer

while True:
  text = input('mafinterp>')
  lexer = Lexer(text)
  tokens = lexer.make_token()
  print(list(tokens))