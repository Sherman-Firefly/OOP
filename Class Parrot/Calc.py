class calculator:
    def __init__(self):
        pass
    def add(self, x,y):
        return x+y
    def sub(self, x,y):
        return x-y
    def mul(self, x,y):
        return x*y
    def div(self, x,y):
        return x/y

calc=calculator()

print(calc.add(2,3))
print(calc.sub(6,3))
print(calc.mul(9,3))
print(calc.div(18,3))


