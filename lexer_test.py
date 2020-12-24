import unittest
import tokens
import lexer

class TestLexer(unittest.TestCase):
    def test_empty(self):
        toks = list(lexer.Lexer("").make_token())
        self.assertEqual(toks, [])
    def test_empty(self):
        toks = list(lexer.Lexer("\t\n ").make_token())
        self.assertEqual(toks, [
            tokens.Token(tokens.TokenType.NEWLINE)
        ])
    def test_numbers(self):
        toks = list(lexer.Lexer("1245.4 .234 1234. .").make_token())
        self.assertEqual(toks, [
            tokens.Token(tokens.TokenType.NUMBER, 1245.4),
            tokens.Token(tokens.TokenType.NUMBER, .234),
            tokens.Token(tokens.TokenType.NUMBER, 1234.),
            tokens.Token(tokens.TokenType.NUMBER, 000.000),
        ])
    def test_operators(self):
        toks = list(lexer.Lexer("+-*/").make_token())
        self.assertEqual(toks, [
            tokens.Token(tokens.TokenType.PLUS),
            tokens.Token(tokens.TokenType.MINUS),
            tokens.Token(tokens.TokenType.MULTIPLY),
            tokens.Token(tokens.TokenType.DIVIDE)
        ])
    def test_par(self):
        toks = list(lexer.Lexer("()").make_token())
        self.assertEqual(toks, [
            tokens.Token(tokens.TokenType.LPAR),
            tokens.Token(tokens.TokenType.RPAR)
        ])
    def test_all(self):
        toks = list(lexer.Lexer("27 + (43 / 36 - 48) * 51").make_token())
        self.assertEqual(toks, [
            tokens.Token(tokens.TokenType.NUMBER, 27),
            tokens.Token(tokens.TokenType.PLUS),
            tokens.Token(tokens.TokenType.LPAR),
            tokens.Token(tokens.TokenType.NUMBER, 43),
            tokens.Token(tokens.TokenType.DIVIDE),
            tokens.Token(tokens.TokenType.NUMBER, 36),
            tokens.Token(tokens.TokenType.MINUS),
            tokens.Token(tokens.TokenType.NUMBER, 48),
            tokens.Token(tokens.TokenType.RPAR),
            tokens.Token(tokens.TokenType.MULTIPLY),
            tokens.Token(tokens.TokenType.NUMBER, 51)
        ]) 