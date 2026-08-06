'''
total = 0

for i in range(1, 5):
    price = float(input(f"Enter price of item {i}: "))
    total += price

print("Total price of the cart =", total)

products = list(map(int,input().split(','))
total = 0
for i in products;
                total = total + i
print(total)

#Password
password = input("Enter password: ")

upper = 0
lower = 0
digits = 0
special = 0

for ch in password:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digits += 1
    else:
        special += 1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
print("Numbers:", digits)
print("Special characters:", special)


#Domain extract(Email.com)
emails = input("Enter email addresses separated by space: ").split()

for email in emails:
    print(email.split("@")[1])
'''
#Movies Lists

movies = input("Enter movie names separated by commas: ").split(",")

for i in range(len(movies)):
    print(i + 1, ".", movies[i].strip())



































