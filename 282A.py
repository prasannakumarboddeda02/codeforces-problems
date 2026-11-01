n = int(input())
x = 0
for i in range(n):
    str = input()
    if str == "X++" or str == "++X":
        x = x + 1
    else:
        x = x - 1
print(x)
    