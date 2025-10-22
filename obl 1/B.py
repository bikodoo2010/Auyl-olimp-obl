n = int(input())
ans=0
for i in range(n):
	s,m = input().split()
	m = int(m)
	if m==5:
		ans+=1
print(ans)