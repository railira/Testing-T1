from _ast import Assign, AsyncFunctionDef, Attribute, BinOp, FunctionDef, Expr
from typing import Any
from ..rule import *

# Warning(’UnusedVariable’, <line number>,’variable ’, <variable name>, ’has not been
# used’)
class UnusedVariableVisitor(WarningNodeVisitor):
    #  Implementar Clase
    def __init__(self):
        super().__init__()
        self.variables = [] #guarda clases de variables
        self.currentClass = None

    def visit_FunctionDef(self, node: ClassDef) -> Any:
        self.currentClass = node.name
        NodeVisitor.generic_visit(self, node)
        
        self.currentClass = None
        if self.variables:
            for i in self.variables:
                self.addWarning("UnusedVariable", i.lineno, "variable " + i.id + " has not been used")
        self.variables = []
                
    def visit_Assign(self, node: Assign) -> Any:
        if self.currentClass is not None:
            self.variables.append(node.targets[0])
            NodeVisitor.generic_visit(self, node)

    def visit_Call(self, node: Attribute) -> Any:
        if self.currentClass is not None:
            for i in self.variables:
                for j in node.args:
                    if i.id == j.id:
                        self.variables.remove(i)
            NodeVisitor.generic_visit(self, node)

    def visit_BinOp(self, node: BinOp) -> Any:
        if self.currentClass is not None:
            for i in self.variables:
                if isinstance(node.left, Name):
                    if i.id == node.left.id:
                        self.variables.remove(i)
                if isinstance(node.right, Name):
                    if i.id == node.right.id:
                        self.variables.remove(i)
            NodeVisitor.generic_visit(self, node)
                            


class UnusedVariableTestRule(Rule):
    #  Implementar Clase
    def analyze(self, node):
        visitor = UnusedVariableVisitor()
        visitor.visit(node)
        return visitor.warningsList()
        
    @classmethod
    def name(cls):
        return 'not-used-variable'
