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
            if node.func.attr == 'assertTrue':
                if isinstance(node.args, Name):
                    if self.variables[node.args.id] == True:
                        self.addWarning("AssertTrueWarning", node.lineno, "useless assert true detected")
                elif isinstance(node.args, Constant):
                    if node.args.value == True:
                        self.addWarning("AssertTrueWarning", node.lineno, "useless assert true detected")

        if isinstance(node.func, Assign):
            self.variables[node.func.targets[0].id] = node.func.value
            print("Hay variables\n \n \n \n \n")
            print(self.variables)
                
        NodeVisitor.generic_visit(self, node)
    

    

class AssertionTrueTestRule(Rule):
    #  Implementar Clase
    def analyze(self, node):
        visitor = AssertionTrueVisitor()
        visitor.visit(node)
        return visitor.warningsList()    
        
    @classmethod
    def name(cls):
        return 'assertion-true'
