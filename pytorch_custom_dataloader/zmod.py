class Zmod:
    def __init__(self, number, mod):
        assert isinstance(number, int)
        assert isinstance(mod, int)
        assert mod >= 1
        self.mod = mod
        self.number = number % mod

    def __add__(self, other: int):
        return Zmod((self.number + other) % self.mod, self.mod)

    def __sub__(self, other: int):
        return Zmod((self.number - other) % self.mod, self.mod)

    def __repr__(self):
        return str(self.number)

    def __str__(self):
        return str(self.number)
