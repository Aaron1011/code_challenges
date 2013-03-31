import string
import re

class ArithmeticSolver:
    def __init__(self):
        self.stack = []
        self.tokens = ['+', '-', '*', '/']

    def get_input(self):
        text = raw_input("Enter an equation: ")
        for char in text.split(' '):
            self.accept_new_token(char)

    def clear_stack(self):
        stack = []

    def accept_new_token(self, token):
        if type(token) == str and re.match(r'\d+', token):
            token = int(token)
        if len(self.stack) < 2:
            self.stack.append(token)
        elif len(self.stack) == 2:
            if self.stack[1] == '*':
                self.stack = [self.stack[0] * token]
            elif self.stack[1] == '/':
                self.stack = [self.stack[0] / token]
            else:
                self.stack.append(token)
        elif len(self.stack) == 3:
            if token == '+':
                self.stack = [self.stack[0] + self.stack[2]]
            elif token == '-':
                self.stack = [self.stack[0] - self.stack[2]]
            self.stack.append(token)
        else:
            op = self.stack.pop()
            if op == '*':
                self.stack[2] = self.stack[2] * token
            elif op == '/':
                self.stack[2] = self.stack[2] / token

    def get_current_answer(self):
        if len(self.stack) == 1:
            return self.stack[0]
        elif self.stack[1] == '+':
            return self.stack[0] + self.stack[2]
        else:
            return self.stack[0] - self.stack[2]
