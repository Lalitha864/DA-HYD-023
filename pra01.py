n = 6
sum = 0

for i in range(1, n):
    if n % i == 0:
        print(i)
        sum += i

print("Sum =", sum)

if sum == n:
    print("Perfect Number")
