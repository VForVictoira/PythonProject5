def factorize_into_three_primes(n):
    primes = []
    candidate = 2

    # 找到第一个素因子
    while candidate * candidate <= n:
        if n % candidate == 0:
            primes.append(candidate)
            n //= candidate
            if len(primes) == 2:  # 找到两个因子后，第三个因子直接是剩下的数
                if is_prime(n):  # 确保剩下的数是素数
                    primes.append(n)
                    return primes
                else:
                    return None
        else:
            candidate += 1

    # 如果最终 n 是素数并且未找到 3 个因子
    if len(primes) == 2 and is_prime(n):
        primes.append(n)
        return primes

    return None  # 无法分解为 3 个素数


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    n = 107184880752592879945112
    result = factorize_into_three_primes(n)
    if result:
        print(f"The three prime factors are: {result}")
    else:
        print("Cannot factorize into three prime numbers.")