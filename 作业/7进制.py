def seven(num):
    # 0s32
    value = list(num)
    for i in range(0, len(value)):
        sum1=0
        sum1 += int(value[i])*7**(len(value)-i-1)
    return sum1

if __name__ == '__main__':
    print(seven('10'))