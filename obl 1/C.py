n = int(input())
arr = list(map(int,input().split()))
arr.sort(reverse=True)
ans = 0
mx = 0
for i in range(1,n+1):
	ans = i*arr[i-1]
	mx = max(ans,mx)
print(mx)