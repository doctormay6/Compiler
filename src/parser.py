#!/usr/bin/python3

from sys import path
import os
path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.token import TokenType
from src.linkedStack import LinkedStack

class NonTerminal(Enum):
    Program     = 0
    Definitions = 1
    Def         = 2
    Formals     = 3
    Nonempty_Formals = 4
    Formal      = 5
    Body        = 6
    Statement_List = 7
    Type        = 8
    Expr        = 9
    Simple_Expr = 10
    Term        = 11
    Factor      = 12
    Actuals     = 13
    Nonempty_Actuals = 14
    Literal     = 15


class Parser:
    def __init__(self):
        stack = LinkedStack()
        stack.push("$")
        parse_table = {
            (NonTerminal.Program, TokenType.program) : [TokenType.program,
                                                        TokenType.identifier,
                                                        TokenType.left_parenthesis,
                                                        NonTerminal.Formals,
                                                        TokenType.right_parenthesis,
                                                        TokenType.semicolon,
                                                        NonTerminal.Definitions,
                                                        NonTerminal.Body,
                                                        TokenType.period]
        }
