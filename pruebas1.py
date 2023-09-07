from ast import *
import ast

print("test_assert_true1")
tree = """def test_x(self):
        x = 2
        self.assertTrue(True)"""
tree = parse(tree)
print(ast.dump(tree,indent=4))
print(tree.body)
print("\n")
print("\n")

print("test_assert_true2")
tree = """def test_x(self):
        self.assertTrue(True)
        x = 2
        self.assertTrue(True)
        print(x)"""
tree = parse(tree)
print(ast.dump(tree,indent=4))
print(tree.body)
print("\n")
print("\n")

