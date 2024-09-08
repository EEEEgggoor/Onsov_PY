S, X = str(input()), str(input())
s1 = S
flag=False
if X in S: flag = True
while True:
    p = (S.lower().split(X.lower()))
    S = ""
    for i in range(len(p)):
        S+=p[i]
    if X in S: flag = True
    else: break

k=""
for i in s1:
    if i.lower() in S:
        k+=i
print(k)