# ACCEPTED
n = input()

n_length = len(n)

counter = 0
if n_length%2 != 0:
    counter+=1

i=0
while i < int(n_length/2):
    if n[i] == n[-(i+1)]:
        counter+=1
    i+=1 

print(counter)

# ALTERNATE VERSION (COMPACT VERSION)
# n = input()
# n_length = len(n)

# # Inline if-else for the odd-length check
# counter = 1 if n_length % 2 != 0 else 0

# # Using a for loop and floor division
# for i in range(n_length // 2):
#     if n[i] == n[-(i + 1)]:
#         counter += 1

# print(counter)