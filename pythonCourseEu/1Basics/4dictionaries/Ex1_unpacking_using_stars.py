#syntax
d = dict([('k1','v1'),('k2','v2'),('k3','v3')])

def unpack(k1 ,k2, k3):
    print(k1, k2, k3)


unpack(**d)

