from _ast import Assert, Assign, Call, FunctionDef
from typing import Any
from ..rule import *
import re

# Warning(’AssertionLessWarning’, <line number>, ’it is an assertion less test’)

class AssertionLessVisitor(WarningNodeVisitor):
    # Implementar Clase
    def __init__(self):
        super().__init__()

    def visit_FunctionDef(self, node: FunctionDef) -> Any:
        
        asserts = 0
        match node:
            case FunctionDef(name=name, args=args, body=body):
                if name.startswith('test_'):
                    for i in body:
                        match i:
                            case Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr=attr, ctx=Load()),
                                                args=args)):
                                regex = re.compile(r'assert')
                                if regex.match(attr):
                                    asserts += 1
                    if asserts == 0:
                        self.addWarning('AssertionLessWarning', node.lineno, 'it is an assertion less test')


class AssertionLessTestRule(Rule):
    def __init__(self):
        super().__init__()

    #  Implementar Clase
    def analyze(self, node):
        visitor = AssertionLessVisitor()
        visitor.visit(node)
        return visitor.warningsList()

        
    @classmethod
    def name(cls):
        return 'assertion-less'


