from tokens import TokenType
from nodes import *

class Parser():
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.advance()
    def raise_error(self):
        raise Exception("Invalid syntax")
    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None
    def parse(self):
        if self.current_token == None:
            return None
        result = self.expression()
        if self.current_token != None:
            self.raise_error()
        return result
    def expression(self):
        result = self.term()
        while self.current_token != None and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            if self.current_token.type == TokenType.PLUS:
                result = AddNode(result, self.term())
                self.advance()
            elif self.current_token.type == TokenType.MINUS:
                result = SubtractNode()
                self.advance()
        return result