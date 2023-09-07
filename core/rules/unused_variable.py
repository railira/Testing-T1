from ..rule import *


class UnusedVariableVisitor(WarningNodeVisitor):
    #  Implementar Clase
    def __init__(self):
        pass


class UnusedVariableTestRule(Rule):
    #  Implementar Clase
    def analyze(self, node):
        visitor = UnusedVariableVisitor()
        visitor.visit(node)
        return visitor.warningsList()
        
    @classmethod
    def name(cls):
        return 'not-used-variable'
