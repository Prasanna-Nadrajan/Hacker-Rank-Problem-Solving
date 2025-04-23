# Enter your code here. Read input from STDIN. Print output to STDOUT
tt=int(input())
for i in range(tt):
    n=int(input())
    nl=set(map(int,input().split()))
    m=int(input())
    ml=set(map(int,input().split()))
    if nl&ml ==nl:
        print("True")
    else:
        print("False")
