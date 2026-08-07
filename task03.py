'''
n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
'''
#while loop
n = int(input("Enter number of terms: "))

a = 0
b = 1
i = 0

while i < n:
    print(a, end=" ")
    a, b = b, a + b
    i += 1
