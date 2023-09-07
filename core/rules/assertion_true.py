from _ast import Call
from typing import Any
from ..rule import *


# Se agregar´a una alerta por cada expresi´on self.asssertTrue(True) dentro
# de una prueba de unidad. La alerta a crear debe tener el siguiente formato:
# 1 Warning(’AssertTrueWarning’, <line number>, ’useless assert true detected’)

class AssertionTrueVisitor(WarningNodeVisitor):

    def __init__(self):
        super().__init__()
        self.variables = {}
    
    #  Implementar Clase
    def visit_Call(self, node: Call):
        if isinstance(node.func, Attribute):
            if node.func.attr == "assertTrue":
                if isinstance(node.args[0], Constant):
                    if node.args[0].value == True:
                        self.addWarning("AssertTrueWarning", node.lineno, "useless assert true detected")
                elif isinstance(node.args[0], Name):
                    if node.args[0].id in self.variables:
                        if self.variables[node.args[0].id] == True:
                            self.addWarning("AssertTrueWarning", node.lineno, "useless assert true detected")

    def visit_Assign(self, node:Assign):
        match node:
            case Assign(targets=[Name(id=variable, ctx=Store())], value=Constant(value=valor, kind=None)):
                self.variables[variable] = valor

                print(f"{variable} = {valor}")

class AssertionTrueTestRule(Rule):
    #  Implementar Clase
    def analyze(self, node):
        visitor = AssertionTrueVisitor()
        visitor.visit(node)
        return visitor.warningsList()    
        
    @classmethod
    def name(cls):
        return 'assertion-true'
