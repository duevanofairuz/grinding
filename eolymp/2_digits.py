n = int(input())

counter=0
if n==0:
    print(1)
else:
    while n!=0:
        n = int(n/10)
        counter+=1
    print(counter)