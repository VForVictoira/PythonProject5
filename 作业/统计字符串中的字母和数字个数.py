string = str(input('请输入一串字符：'))
list = [s for s in string]
letter =[l for l in list if l.isalpha()]
num = [n for n in list if n.isdigit()]

print(f'该字符串字母个数为{len(letter)}')
print(f'该字符串数字个数为{len(num)}')