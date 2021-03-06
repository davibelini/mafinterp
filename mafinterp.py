from interpreter import Interpreter
import sys
from lexer import Lexer
from parse import Parser

if len(sys.argv) > 1:
  if sys.argv[1] == "-f" or sys.argv[1] == "--file":
    if sys.argv[2].split(".")[1] == "maf":
      with open(sys.argv[2], "r") as f:
        lexer = Lexer(text=f.read())
        print(list(lexer.make_token()))
    else:
      print("ERROR: File must have 'maf' extension.")
  else:
    print("ERROR: Unknown option inputted")
else:
  while True:
    try:
      text = input('mafinterp >')
      if text == 'quit' or text == 'end' or text =='exit':
        quit()
      lexer = Lexer(text)
      tokens = lexer.make_token()
      parser = Parser(tokens)
      tree = parser.parse()
      if not tree:
        continue
      interpreter = Interpreter()
      print(interpreter.visit(tree))
    except Exception as e:
      print(e)
