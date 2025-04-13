import itertools

tl=list(map(int,input().split()))
lists=[]
t=tl[0]
for i in range(t):
    lists.append(list(map(int,input().split()))[1::])
M = tl[1]

combinations = itertools.product(*lists)
max_value = 0

for combo in combinations:
    current_value = sum(x**2 for x in combo) % M
    max_value = max(max_value, current_value)
print(max_value)
