class Math():
    def __init__(self):
        self.math = [5, 7, 10]
    def mult(self):
        return [a * 3 for a in self.math]
    def sub(self):
        return [a - 5 for a in self.math]


m = Math()
print(m.mult())
print(m.sub())
