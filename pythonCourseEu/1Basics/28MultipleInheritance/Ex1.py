#Diamond problem

class A:
    def m(self):
        print("m of A called")


class B(A):
    def m(self):
        print("m of B called")


class C(A):
    def m(self):
        print("m of C called")


class D(B, C):
    pass

class E(C, B):
    pass

x = D()
x.m()

y = E()
y.m()