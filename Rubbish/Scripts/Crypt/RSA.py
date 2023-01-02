from random import randrange


def generate_n_bit_odd(n: int):
    assert n > 1
    return randrange(2 ** (n - 1) + 1, 2 ** n, 2)


first_50_primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
                   37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
                   79, 83, 89, 97, 101, 103, 107, 109, 113, 127,
                   131, 137, 139, 149, 151, 157, 163, 167, 173, 179,
                   181, 191, 193, 197, 199, 211, 223, 227, 229, 233]


def get_lowlevel_prime(n):
    while True:
        c = generate_n_bit_odd(n)

        for divisor in first_50_primes:
            if c % divisor == 0 and divisor ** 2 <= c:
                break
        else:
            return c


def miller_rabin_primality_check(n, k=20):
    assert n > 3
    if n % 2 == 0:
        return False

    s, d = 0, n - 1
    while d % 2 == 0:
        d >>= 1
        s += 1

    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(s):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True


def get_random_prime(num_bits):
    while True:
        pp = get_lowlevel_prime(num_bits)
        if miller_rabin_primality_check(pp):
            return pp


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a // gcd(a, b) * b


def exgcd(a, b):
    old_s, s = 1, 0
    old_t, t = 0, 1
    while b:
        q = a // b
        s, old_s = old_s - q * s, s
        t, old_t = old_t - q * t, t
        a, b = b, a % b
    return a, old_s, old_t


def invmod(e, m):
    a = e
    b = m
    old_s, s = 1, 0
    old_t, t = 0, 1
    while b:
        q = a // b
        s, old_s = old_s - q * s, s
        t, old_t = old_t - q * t, t
        a, b = b, a % b
    g, x, y = a, old_s, old_t

    assert g == 1

    if x < 0:
        x += m
    return x


def encrypt(plain_bytes: bytes, e, n):

    int_data = int.from_bytes(plain_bytes, 'big')
    return pow(int_data, e, n)


def decrypt(encrypted_int_data: int, d, n):
    int_data = pow(encrypted_int_data, d, n)
    if int_data == 0:
        return bytes(1)
    return int_data.to_bytes((int_data.bit_length() + 7) // 8, 'big')


if __name__ == "__main__":
    key_length = 512
    e = 3
    p = get_random_prime(key_length // 2)
    q = get_random_prime(key_length // 2)
    while gcd(e, lcm(p - 1, q - 1)) != 1:
        p = get_random_prime(key_length // 2)
        q = get_random_prime(key_length // 2)
    n = p * q
    d = invmod(e, lcm(p - 1, q - 1))

    with open("plain.txt", "rb") as f:
        data = f.read()
    print(data)
    data2 = encrypt(data, e, n)
    print(data2)
    data3 = decrypt(data2, d, n)
    print(data3)
    print(str(data3, encoding="gb2312"))
