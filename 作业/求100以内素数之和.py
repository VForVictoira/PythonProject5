def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_primes(limit):
    """计算指定范围内素数的和"""
    return sum(num for num in range(2, limit + 1) if is_prime(num))

if __name__ == '__main__':
    result = sum_primes(100)
    print(f"100以内素数之和为：{result}")