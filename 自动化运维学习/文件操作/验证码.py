import random
import string

def generate_verification_code():
    letters_and_digits = string.ascii_uppercase + string.digits
    code = ''.join(random.choice(letters_and_digits) for _ in range(4))
    return code

# 生成验证码
verification_code = generate_verification_code()
print("生成的验证码是:", verification_code)
