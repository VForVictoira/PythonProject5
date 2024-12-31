from fractions import Fraction

def even_Number_calc(n):
    return sum(Fraction(1, i) for i  in range(2, n + 1, 2))

def odd_Number_calc(n):
    return sum(Fraction(1, i) for i in range(1, n + 1,2))

def odd_Or_Even(n):
    if n % 2 == 0:
        return even_Number_calc(n)
    else:
        return odd_Number_calc(n)

if __name__ == '__main__':
    n = int(input('请输入一个整数：'))
    result = odd_Or_Even(n)
    print(f'和为：{result}')