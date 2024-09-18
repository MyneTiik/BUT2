class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

class Constante(Node):
    def __init__(self, value):
        super().__init__()
        self.data = value

    def resolve(self):
        return self.data

class Plus(Node):
    def resolve(self):
        return self.left.resolve() + self.right.resolve()

class Moins(Node):
    def resolve(self):
        return self.left.resolve() - self.right.resolve()

class Fois(Node):
    def resolve(self):
        return self.left.resolve() * self.right.resolve()

class Divise(Node):
    def resolve(self):
        return self.left.resolve() / self.right.resolve()

# Example usage:
# Constructing the expression (3 + 5) * (10 - 2)
root = Moins(Plus(Constante(3), Fois(Constante(2), Constante(6))), Fois(Constante(2), Plus(Constante(4), Constante(9))))

result = root.resolve()
print(f"Result: {result}")  # Output: Result: 64