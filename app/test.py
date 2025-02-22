class a:
    def __init__(self, a):
        self.a = a
    def __eq__(self, value):
        return value.a == self.a
    

woah1 = a(1)
woah2 = a(1)

lista = [woah2]

print(woah1 in lista)