from ast import *
import ast

print("test_with_assertion")
tree = """def test_x(self):
        x = 2
        y = 3
        self.assertEquals(2,3)"""
tree = parse(tree)
print(ast.dump(tree,indent=4))
print(tree.body)
print("\n")
print("\n")

print("test_without_assertion")
tree = """class TestCase():
        def test_x(self):
                x = 2
                y = 3"""
tree = parse(tree)
print(ast.dump(tree,indent=4))
print(tree.body)
print("\n")
print("\n")

print("test_without_multiple_assertion")
tree = """class TestCase():
        def test_x(self):
                x = 2

        def test_y(self):
                y = 5"""
tree = parse(tree)
print(ast.dump(tree,indent=4))
print(tree.body)
