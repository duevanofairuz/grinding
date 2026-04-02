n = int(input())

decimals = []
b = format(n, 'b')
itr = len(b)

for i in range(itr):
    b = b[1:] + b[0]
    temp = int(b, 2)
    decimals.append(temp)

# decimals.sort(reverse=True)
print(max(decimals))