import random
from math import pow

a = random.randint(2,10)


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)


# x = mulinv(b) mod n, (x * b) % n == 1
def mulinv(b, n):
    g, x, _ = egcd(b, n)
    print(g, x, _)
    if g == 1:
        return x % n

def b(m, km, x, p):
    return (km * (m - x * a)) % (p - 1)

def multiplicative_inverse(e, phi):
    for x in range(1, phi):
        if (((e % phi) * (x % phi)) % phi == 1):
            return x
    return -1

def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)

def phi(n):
    result = [i for i in range(1, n + 1) if gcd(n, i) == 1]
    return len(result)

def m(x, a, k, b, p):
    return ((x * a + k * b) % (p-1))

# 1
def get_y(p, g):
    x = random.randint(0, p-1)
    x = 8
    return (g ** x) % p

def get_key_ext1(p, g):
    x = random.randint(0, p-1)
    x = 8
    return (g**x)%p


#For key generation i.e. large random number
def gen_key(q):
    key= random.randint(pow(10,20),q)
    while gcd(q,key)!=1:
        key=random.randint(pow(10,20),q)
    return key

def power(a,b,c):
    x=1
    y=a
    while b>0:
        if b%2==0:
            x=(x*y)%c;
        y=(y*y)%c
        b=int(b/2)
    return x%c

#For asymetric encryption
def encryption(msg,q,h,g):
    ct=[]
    k=gen_key(q)
    s=power(h,k,q)
    p=power(g,k,q)
    for i in range(0,len(msg)):
        ct.append(msg[i])
    print("g^k used= ",p)
    print("g^ak used= ",s)
    for i in range(0,len(ct)):
        ct[i]=s*ord(ct[i])
    return ct,p

#For decryption
def decryption(ct,p,key,q):
    pt=[]
    h=power(p,key,q)
    for i in range(0,len(ct)):
        pt.append(chr(int(ct[i]/h)))
    return pt


#msg=input("Enter message.")
#q = random.randint(pow(10,20),pow(10,50))
g = 2
p = 11
y = get_y(p, g)
print("y = ", y)
public = (y, g, p)
print("public", public)
x = 8
print("private", x)
k = phi(p)-1
print("k=", k)
a = (g ** k) % p
print("a = ", a)
#m = m(x, a, k, b, p)

km1=multiplicative_inverse(k, p-1)
print("km1 = ", km1)
print(mulinv(k, p-1))

m = 5
b = b(m, km1, x, p)
print("b = ", b)
sign =(a, b)
print("Подпись ", m, " = ", sign)



'''
key=gen_key(q)
h=power(g,key,q)
print("g used=",g)
print("g^a used=",h)
ct,p=encryption(msg,q,h,g)
print("Original Message=",msg)
print("Encrypted Maessage=",ct)
pt=decryption(ct,p,key,q)
d_msg=''.join(pt)
print("Decryted Message=",d_msg)
'''