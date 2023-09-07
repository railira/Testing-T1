from _ast import BinOp, FunctionDef, Expr
from typing import Any
from ..rule import *


class UnusedVariableVisitor(WarningNodeVisitor):
    #  Implementar Clase
    def __init__(self):
        super().__init__()
        self.variables = {}

    def visit_Assign(self, node):
        print("variable encontrada\n\n\n\n")
        match node:
            case Assign(
                targets=[Name(id=p, ctx=Store())],
                  value=Constant(value=valor, kind=None)):
                self.variables[p] = [valor, node.lineno]
            case Assign(
                targets=[Name(id=p, ctx=Store())],
                    value=BinOp(left=xx, op=op, right=yy)):
                self.variables[p] = [valor, node.lineno]
                node.generic_visit(self)
  

    def visit_Expr(self, node: FunctionDef) -> Any:
        print("assert encontrado\n\n\n\n")
        print(self.variables)
        match node:
            case Expr(name=name, args=args, body=body):
                for i in body:
                    match i:
                        case Call(func=Attribute(value=Name(id='self', ctx=Load()), attr=attr, ctx=Load()),
                                    args=args):
                            
                            if isinstance(args[0], Constant):
                                if args[0].id in self.variables:
                                    self.variables.pop(args[0].id)
                            elif isinstance(args[0], Name):
                                pass
        
        for i in self.variables:
            self.addWarning('UnusedVariable', self.variables[i][1], f'variable {i} has not been used')
                            


class UnusedVariableTestRule(Rule):
    #  Implementar Clase
    def analyze(self, node):
        visitor = UnusedVariableVisitor()
        visitor.visit(node)
        return visitor.warningsList()
        
    @classmethod
    def name(cls):
        return 'not-used-variable'
