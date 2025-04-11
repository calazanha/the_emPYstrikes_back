class Contador:
    def __init__(self, max):
        self.max = max
        self.atual = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.atual <= self.max:
            val = self.atual
            self.atual += 1
            return val
        else:
            raise StopIteration

for num in Contador(5):
    print(num)
