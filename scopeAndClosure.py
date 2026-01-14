def chaiCoder(num):
    def actual(x):
        return num ** x
    return actual

f = chaiCoder(2)
print(f(3))