from ast import *
from core.rewriter import RewriterCommand


class InlineCommand(RewriterCommand):
    # Implementar comando, recuerde que puede necesitar implementar además clases NodeTransformer y/o NodeVisitor.
    def apply(self, node):
        rewriter = InlineRewriter()
        return rewriter.visit(node)
    

class InlineRewriter(ast.NodeTransformer):

    def __init__():
        super().__init__()
        self.currentClass = None
        self.variables = {}

    def visit_FunctionDef(self, node: FunctionDef) -> Any:
        if self.currentClass is not None:
            if node.name.startswith("test_"):
                self.variables = {}
                NodeVisitor.generic_visit(self, node)
                self.variables = {}
        return node
