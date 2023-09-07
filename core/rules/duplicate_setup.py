from _ast import ClassDef, FunctionDef
import ast
from typing import Any
from ..rule import *

# Debe asumir que los test solo tendr´an test-clases, es decir, que ser´an clases
# donde todos su m´etodos son tests. Se debe lanzar una alerta si todos los test de la clase tiene al menos una
# linea en com´un al inicio.

class DuplicatedSetupVisitor(WarningNodeVisitor):
    #  Implementar Clase
    def __init__(self):
        super().__init__()
        self.body_function = []
        self.currentClass = None
        self.count = 0
        self.min_count = 200
        self.duplicated = []
        self.first = True

    def visit_ClassDef(self, node: ClassDef) -> Any:
        self.currentClass = node.name
        NodeVisitor.generic_visit(self, node)
        self.currentClass = None
        
        if self.min_count != 200:
            self.addWarning("DuplicatedSetup", str(self.min_count), "there are " + str(self.min_count) + " duplicated setup statements")

        self.duplicated = []
        self.count = 0
        self.first = True

    def visit_FunctionDef(self, node: FunctionDef) -> Any:
        if self.currentClass is not None:
            if node.name.startswith("test_"):
                if self.first:
                    self.body_function = node.body
                    self.first = False
                else:
                    for i in range(len(self.body_function)):
                            print(ast.dump(self.body_function[i], indent=4))
                            print("----------------------\n\n")
                            print(ast.dump(node.body[i], indent=4))
                            print("\n\n")
                            
                            if ast.dump(self.body_function[i]) == ast.dump(node.body[i]):
                                print("iguales")
                                self.count += 1
                            else:
                                break

                    if self.count < self.min_count and self.count != 0:
                        self.min_count = self.count
                        self.count = 0

            

class DuplicatedSetupRule(Rule):
    #  Implementar Clase
    def analyze(self, node):
        visitor = DuplicatedSetupVisitor()
        visitor.visit(node)
        return visitor.warningsList()

    @classmethod
    def name(cls):
        return 'duplicate-setup'
