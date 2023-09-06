from ast import *
import ast

print("test_assert_true1")
tree = """def test_x(self):
                            x = True
                            self.assertTrue(x)"""
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

print("test_assert_true_variable_True")
tree = """def test_x(self):
        x = True
        self.assertTrue(x)"""
tree = parse(tree)
print(ast.dump(tree,indent=4))
print("\n")
print("\n")

print("test_assert_true_no_warning")
tree = """def test_x(self):
        x = False
        self.assertTrue(x)
        self.assertTrue(False)"""
tree = parse(tree)
print(ast.dump(tree,indent=4))
print("\n")
print("\n")

print("test_assert_true_no_warning2")
tree = """def test_x(self):
        x = 5
        self.assertEqual(x, 5)"""
tree = parse(tree) 
print(ast.dump(tree,indent=4))
print("\n")
print("\n")

print("test_assert_true_mix")
tree = """def test_x(self):
        x = 9
        y = True
        self.assertTrue(True)
        self.assertEqual(x, 9)
        self.assertTrue(y)"""
tree = parse(tree)
print(ast.dump(tree,indent=4))
print("\n")
print("\n")

print("test_assert_multiple")
tree = """def test_x(self):
        x = 9
        y = True
        self.assertTrue(True)
        self.assertEqual(x, 9)
        self.assertTrue(y)"""
tree = parse(tree)
print(ast.dump(tree,indent=4))
