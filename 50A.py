m,n = map(int, input().split())
total = (m//2)*n
if m%2==1:
    total = total + (n//2)
print(total)