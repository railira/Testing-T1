from ast import *
import ast
from core.rewriter import RewriterCommand


class AssertTrueCommand(RewriterCommand):
    # Implementar comando, recuerde que puede necesitar implementar además clases NodeTransformer y/o NodeVisitor.

    def apply(self, node):
        rewriter = AssertTrueRewriter()
        return rewriter.visit(node)


class AssertTrueRewriter(ast.NodeTransformer):
    def visit_Call(self, node):
        if (
            isinstance(node.func, ast.Attribute)
            and node.func.attr == "assertEquals"
            and len(node.args) == 2
            and isinstance(node.args[0], ast.Name)  
            and isinstance(node.args[1], ast.NameConstant)  
        ):
            if node.args[1].value is True:
                new_call = ast.Call(
                    func=ast.Attribute(value=node.func.value, attr="assertTrue", ctx=ast.Load()),
                    args=[node.args[0]],
                    keywords=[],
                )
                return new_call
        return node