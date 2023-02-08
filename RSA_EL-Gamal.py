import random
from math import pow
####################################################

# Евклид - Наибольший Общий Делитель -
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Расширенный алгоритм Евклида - Наибольший Общий Делитель -
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

#======================================================================#
#Алгоритм Евклида поиска мультипликативно обратного элемента по модулю #
#======================================================================#
def mul_inv1(e, phi):
    for x in range(1, phi):
        if (((e % phi) * (x % phi)) % phi == 1):
            return x
    return -1

#--------------------------------------------------#
# Определяем принадлежность числа к простым        #
#--------------------------------------------------#

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num ** 0.5) + 2, 2):
        if num % n == 0:
            return False
    return True

def RSA_generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Оба числа должны быть простые')
    elif p == q:
        raise ValueError('p и q не могут быть равны')

    n = p * q

    # Вычисляем значение функции Эйлера от n
    phi = (p - 1) * (q - 1)

    # Выбираем случайным образом открытый ключ с учётом выполнения условий 1 < e <= phi(n) и НОД (e, phi) =1
    e = random.randrange(1, phi)

    # алгоритмом Евклида находим НОД (the greatest common divisor - gcd)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    #Евклидом генерим закрытый ключ...
    d = mul_inv1(e, phi)

    # Открытый ключ (e, n) Закрытый ключ (d, n)
    return ((e, n), (d, n))

def RSA_verify(pk, s):
    key, n = pk
    return s **key % n

######################### EL-Gamal #################################################

a = random.randint(2,10)


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

def phi(n):
    result = [i for i in range(1, n + 1) if gcd(n, i) == 1]
    return len(result)

def m(x, a, k, b, p):
    return ((x * a + k * b) % (p-1))


def get_y(p, g):

def get_key_ext1(p, g):
    x = random.randint(0, p-1)
    x = 8
    return (g**x)%p

def gen_key(q):
    key= random.randint(pow(10,20),q)
    while gcd(q,key)!=1:
        key=random.randint(pow(10,20),q)
    return key

def power(a, b, c):
    x = 1
    y = a
    while b > 0:
        if b % 2==0:
            x = (x * y) % c;
        y = (y * y) % c
        b = int(b / 2)
    return x % c

def task_answer():
    g = 2
    p = 11
    x = random.randint(0, p-1)
    y =  (g ** x) % p
    print("g = ", g, "p = ", p, "y = ", y)
    public = (y, g, p)
    print("Открытый ключ: ", public)
    k = phi(p) - 1
    print("k = ", k)
    a = (g ** k) % p
    print("a = ", a)



if __name__ == '__main__':

    print("Лабораторная работа 8, вариант 10. ЭЦП по алгоритму RSA")
    p = 3
    q = 11

    print("RSA: p = ", p, "q = ", q)
    print("RSA: Генерация пары закрытого и открытого ключа . . .")
    public, private = RSA_generate_keypair(p, q)
    print("Открытый ключ: ", public, " Закрытый ключ: ", private)

    print("Проверка подлинности подписанных по алгоритму RSA хэш-значений некоторых сообщений для заданных открытых ключей")
    public = (79, 221)
    sign = 142
    print("Проверка подписи для открытого ключа ", public, "ЭЦП", sign)
    m = RSA_verify(public, sign)
    print("Получен хэш", m, "сравниваем с 207")

    sign = 9
    print("Проверка подписи для открытого ключа ", public, "ЭЦП", sign)
    m = RSA_verify(public, sign)
    print("Получен хэш", m, "сравниваем с 112")

    sign = 147
    print("Проверка подписи для открытого ключа ", public, "ЭЦП", sign)
    m = RSA_verify(public, sign)
    print("Получен хэш", m, "сравниваем с 82")
    print("")
    print("Лабораторная работа 8, вариант 10. ЭЦП по алгоритму Эль-Гамаль")
    print("Ищем открытый ключ для указанных в варианте секртентных параметров и строим подпись для хэш-значения")
    print("")

