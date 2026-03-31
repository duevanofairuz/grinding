# n = int(input())

# if n==1:
#     print(10, 0)
# elif n>1:
#     exp = 10**(n-1)
#     sumN = 9 * exp
#     smallN = 10 ** (n-1)
#     print(sumN, smallN)

# counter = 0
# for i in range (100, 999):
#     first = int(i/10)
#     second = i%10
#     third = i%10
#     if (first * second) == (first + second):
#         counter+=1
#         print(i)

# print('TOTAL: ', counter)

# sum = 0
# mul = 1
# n = 324
# while n!=0:
#     sum = sum + (n%10)
#     mul = mul * (n%10)
#     n = int(n/10)

# print('sum: ', sum, 'mul:', mul)

N = int(input())
tempN = N
N -=1
start = 10**(N)
end = 9
while N!=0:
    end = end*10+9
    N-=1

arr = []
counter = 0
for i in range (start, end):
    temp = i
    sum = 0
    mul = 1
    while temp !=0:
        sum = sum + (temp%10)
        mul = mul * (temp%10)
        temp = int(temp/10)
    if sum == mul:
        counter+=1
        # print(i)
        arr.append(i)
# print(arr[0])
# print(counter)
if tempN == 1:
    print(10, 0)
else:
    print(counter, arr[0])

