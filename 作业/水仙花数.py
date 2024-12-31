def is_narcissistic(num):
    """判断一个数是否为水仙花数"""
    digits = list(map(int, str(num)))  # 将数字转为各个位的数字列表
    n = len(digits)  # 数字的位数
    return sum(d**n for d in digits) == num

def find_narcissistic_numbers(start, end):
    """寻找指定范围内的所有水仙花数"""
    return [num for num in range(start, end + 1) if is_narcissistic(num)]

if __name__ == '__main__':
    # 寻找三位数的水仙花数
    narcissistic_numbers = find_narcissistic_numbers(100, 999)
    print("三位数的水仙花数有：", narcissistic_numbers)