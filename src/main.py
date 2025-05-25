print('Hello World')
# 修改main.p内容
def add(a, b):
    return a + b

# 增加减法功能
def subtract(a, b):
    return a - b


if __name__ == "__main__":
    print("2 + 3 =", add(2, 3))
    print("5 - 3 =", subtract(5, 3))