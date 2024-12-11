import random
from sympy import mod_inverse, isprime

# функция для генерации двух больших простых чисел
def generate_prime(candidate_start=100, candidate_end=200):
    while True:
        candidate = random.randint(candidate_start, candidate_end)
        if isprime(candidate):
            return candidate

# генерация ключей RSA
def generate_keys():
    p = generate_prime()
    q = generate_prime()
    while p == q:
        q = generate_prime()
    n = p * q
    phi = (p - 1) * (q - 1)

    # выбор e, такого что 1 < e < phi и e взаимно просто с phi
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    # определение d, такого что (d * e) % phi = 1
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

# вспомогательная функция для вычисления НОД
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# функция шифрования
def encrypt(public_key, plaintext):
    e, n = public_key
    encrypted_message = [pow(ord(char), e, n) for char in plaintext]
    return encrypted_message

# функция дешифрования
def decrypt(private_key, encrypted_message):
    d, n = private_key
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in encrypted_message])
    return decrypted_message

print("Генерация ключей RSA...")
public_key, private_key = generate_keys()
print(f"Открытый ключ: {public_key}")
print(f"Закрытый ключ: {private_key}")

message = input("Введите сообщение для шифрования: ")

encrypted_message = encrypt(public_key, message)
print(f"Зашифрованное сообщение: {encrypted_message}")

decrypted_message = decrypt(private_key, encrypted_message)
print(f"Расшифрованное сообщение: {decrypted_message}")
