n,k = map(int, input().split())
nums = list(map(int, input().split()))
flag = n
for i in range(0,n):
    if nums[i]<nums[k-1] or nums[i]<=0:
        flag = i
        break
print(flag)