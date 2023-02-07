import random

# Евклид - Наибольший Общий Делитель -
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#======================================================================#
#Алгоритм Евклида поиска мультипликативно обратного элемента по модулю #
#======================================================================#

def multiplicative_inverse(e, phi):
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


def generate_keypair(p, q):
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
    d = multiplicative_inverse(e, phi)

    # Открытый ключ (e, n) Закрытый ключ (d, n)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    key, n = pk
    # Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [((ord(char)-48) ** key) % n for char in plaintext]

    # Return the array of bytes
    return cipher

def decrypt(pk, ciphertext):

    key, n = pk
    plain = [((int ** key) % n) for int in ciphertext]
    return ''.join(str(x) for x in plain)

def verify(pk, s):
    key, n = pk
    return s **key % n

if __name__ == '__main__':
    print("RSA Шифрование/ Расшифровка")
    p = 3
    q = 11
    print("Генерация пары закрытого и открытого ключа . . .")
    public, private = generate_keypair(p, q)

    print("Открытый ключ: ", public, " Закрытый ключ: ", private)

    message = input("Enter a message to encrypt with your private key: ")
    #message = "312"
    encrypted_msg = encrypt(public, message)

    print("Зашифрованное сообщение: ")
    print(''.join(map(lambda x: str(x), encrypted_msg)))

    print("Расшифрованное закрытым ключом сообщение: ",private , " . . .")
    print("Сообщение : ")
    print(decrypt(private, encrypted_msg))
    public = (79, 221)
    sign = 142
    print("Проверка подписи для  ключа ", public, "ЭЦП", sign, "...")
    v = verify(public, sign)
    print(v)

    sign = 9
    print("Проверка подписи для  ключа ", public, "ЭЦП", sign, "...")
    v = verify(public, sign)
    print(v)

    sign = 147
    print("Проверка подписи для  ключа ", public, "ЭЦП", sign, "...")
    v = verify(public, sign)
    print(v)
