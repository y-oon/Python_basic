def test():
    print("A 지점 통과")
    yield 1
    print("B 지점 통과")
    yield 2
    print("C 지점 통과")

output = test()  # 출력x

print("D 지점 통과")
a = next(output)
print(a)  # 1
print("E 지점 통과")
b = next(output)
print(b)  # 2
print("F 지점 통과")
c = next(output)
print(c) # StopIteration