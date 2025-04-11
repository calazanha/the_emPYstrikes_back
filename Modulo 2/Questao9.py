class Animal:
    def fazer_som(self):
        print("Som genérico de animal")

class Cachorro(Animal):
    def fazer_som(self):
        print("Au au!")

class Gato(Animal):
    def fazer_som(self):
        print("Miau!")

c = Cachorro()
g = Gato()
c.fazer_som()
g.fazer_som()
