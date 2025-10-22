n = int(input())
a = list(map(int, input().split()))
S = sum(a)
k = S // n
r = S % n
a.sort(reverse=True)
ans = 0
for i in range(n):
    t = k + 1 if i < r else k
    if a[i] > t:
        ans += a[i] - t
print(ans)
