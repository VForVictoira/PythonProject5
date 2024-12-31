A = [3,6,9]
user_input = input("请输入一组数字，用空格分隔: ")  # 用户输入示例: 1,2,3,4,5
B = [int(x) for x in user_input.split(' ')]

SUM = sum(a*b for a,b in zip(A,B))
print(f'A 和 B 两个列表的累加和是{SUM}')