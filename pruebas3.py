from ast import *
import ast

print("test_unuse_variable")
tree = """def test_x(self):
        x = 2
        y = 3
        self.assertEquals(2,3)"""

tree = parse(tree)
print(ast.dump(tree,indent=4))
print(tree.body)
print("\n")
print("\n")

print("test_unused_variable2")
tree = """class TestCase():
        def test_x(self):
                x = 2
                y = 3"""

tree = parse(tree)
print(ast.dump(tree,indent=4))
print(tree.body)
print("\n")
print("\n")

print("test_unused_variable3")
tree = """class TestCase():
        def test_x(self):
                x = 2
                y = 3

        def test_y(self):
                y = 5"""

tree = parse(tree)
print(ast.dump(tree,indent=4))
print(tree.body)
print("\n")
print("\n")

print("test_unused_variable4")
tree = """class TestCase():


    def test_x(self):
        x = 2
        y = 2
        z = False
        self.assertTrue(z)

    def test_y(self):
        x = 2
        y = x + 2
        z = False
        self.assertTrue(z)"""

tree = parse(tree)
print(ast.dump(tree,indent=4))
print(tree.body)
print("\n")
print("\n")
