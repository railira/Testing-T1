from ast import *
import ast

print("usando test duplicated setup")
print("Test_assert_true1")

tree = """class TestX(TestCase):
    def test_x(self):
        x = 2
        y = 2
        self.assertEquals(x,y)
    def test_y(self):
        x = 2
        y = 2
        self.assertEquals(y,x)"""
tree = parse(tree)
print(ast.dump(tree,indent=4))
print(tree.body)
print("\n")
print("\n")

print("Test_assert_true2")
tree = """class TestX(TestCase):
    def test_x(self):
        x = 2
        y = 2
        z = 5
        self.assertEquals(x,y)

    def test_y(self):
        x = 2
        g = 2
        z = 5
        f = 5
        self.assertEquals(y,x)"""
tree = parse(tree)
print(ast.dump(tree,indent=4))
print(tree.body)
print("\n")
print("\n")

print("Test_assert_true3")
tree = """class TestX(TestCase):
    def test_x(self):
        x = 1
        y = 2
        z = 5
        self.assertEquals(x,y)

    def test_y(self):
        x = 2
        g = 2
        z = 5
        f = 5
        self.assertEquals(y,x)"""
tree = parse(tree)
print(ast.dump(tree,indent=4))
print(tree.body)
print("\n")
print("\n")

print("Test_assert_true4")
tree = """class TestX(TestCase):
    def test_x(self):
        x = 5
        g = 3
        z = 1
        f = "a"
        self.assertEquals(z,f)"""
tree = parse(tree)
print(ast.dump(tree,indent=4))
print(tree.body)
print("\n")
print("\n")

print("test_assert_true5")
tree = """class TestX(TestCase):
    def test_x(self):
        x = 5
        g = 3
        self.assertEquals(x,5)
    def test_y(self):
        x = 5
        g = 3
        self.assertEquals(g,3)
    def test_z(self):
        x = 5
        g = 3
        f = "a"
        self.assertEquals(x+g,8)"""
tree = parse(tree)
print(ast.dump(tree,indent=4))
print(tree.body)
print("\n")
print("\n")

print("test_assert_true5")
tree = """class TestX(TestCase):
    def test_x(self):
        y = 5
        h = 3
        self.assertEquals(y,5)
    def test_y(self):
        x = 5
        g = 3
        self.assertEquals(g,3)
    def test_z(self):
        x = 5
        g = 3
        f = "a"
        self.assertEquals(x+g,8)"""
tree = parse(tree)
print(ast.dump(tree,indent=4))
print(tree.body)
print("\n")
print("\n")
