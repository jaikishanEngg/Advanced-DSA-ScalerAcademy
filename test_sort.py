class A:
    def __init__(self, l):
        self.l = l

listofA = [A(4), A(3), A(1), A(2), A(8)]
print(sorted(listofA, key = lambda x: x.l))