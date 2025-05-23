# Enter your code here. Read input from STDIN. Print output to STDOUT
u=[]
l=[]
od=[]
ed=[]
s=input().strip()
for i in s:
    if i.isupper():
        u.append(i)
    elif i.islower():
        l.append(i)
    elif i.isdigit():
        if(int(i)%2==0):
            ed.append(i)
        else:
            od.append(i)
print("".join(["".join(sorted(l)),"".join(sorted(u)),"".join(sorted(od)),"".join(sorted(ed))]))
