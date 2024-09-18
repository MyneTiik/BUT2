#Sert a l'héritage pour définir un fils droit/gauche
class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

#la constante défini un nombre qui n'a pas besoin d'être calculé

class Constante(Node):
    def __init__(self, value):
        super().__init__()
        self.data = value

    def resolve(self):
        return self.data

# on creer des classes pour chacunes des opérations

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

root = Moins(Plus(Constante(3), Fois(Constante(2), Constante(6))), Fois(Constante(2), Plus(Constante(4), Constante(9))))

result = root.resolve()
print(f"Result: {result}")
