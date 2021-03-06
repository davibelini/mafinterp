from tokens import TokenType
from nodes import *

class Parser():
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.advance()
    def raise_error(self):
        raise Exception("Invalid syntax.")
    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None
    def parse(self):
        if self.current_token == None:
            return None
        result = self.get_expression()
        if self.current_token != None:
            self.raise_error()
        return result
    def get_expression(self):
        result = self.get_term() # If there is only multiplication or division
        while self.current_token != None and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            if self.current_token.type == TokenType.PLUS: 
                self.advance()
                result = AddNode(result, self.get_term())
            elif self.current_token.type == TokenType.MINUS:
                self.advance()
                result = SubtractNode(result, self.get_term())
        return result
    def get_term(self):
        result = self.get_factor() # return factor if there is no umltiply or divide operation
        while self.current_token != None and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
            if self.current_token.type == TokenType.MULTIPLY:
                self.advance()
                result = MultiplyNode(result, self.get_factor())
            elif self.current_token.type == TokenType.DIVIDE:
                self.advance()
                result = DivideNode(result, self.get_factor())

        return result
    def get_factor(self):
        token = self.current_token

        if token.type == TokenType.LPAR:
            self.advance()
            result = self.get_expression()

            if self.current_token.type != TokenType.RPAR:
                self.raise_error()
            
            self.advance()
            return result
        if token.type == TokenType.NUMBER:
            self.advance()
            return NumberNode(token.value)
        elif token.type == TokenType.PLUS:
            self.advance()
            return PlusNode(self.get_factor())
        elif token.type == TokenType.MINUS:
            self.advance()
            return MinusNode(self.get_factor())
        else:
            self.raise_error()