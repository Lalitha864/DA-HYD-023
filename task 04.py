'''
#take a list 4,6,1,0,2,4,0,6 take as input and output should be boundaries and total scores and dot balls give an python code

runs = list(map(int, input("Enter runs: ").split()))

score = 0
boundaries = 0
dots = 0

for i in runs:
    score = score + i

    if i == 4 or i == 6:
        boundaries = boundaries + 1

    if i == 0:
        dots = dots + 1

print("Total Score:", score)
print("Boundaries:", boundaries)
print("Dot Balls:", dots)


password = "1234"
chance = 5

while chance > 0:
    user = input("Enter Password: ")

    if user == password:
        print("Phone Unlocked")
        break
    else:
        chance = chance - 1
        print("Wrong Password")
        print("Chances Left:", chance)

if chance == 0:
    print("Phone Locked")
'''
balance = 5000

while True:
    print("\n1. Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Balance:", balance)

    elif choice == 2:
        amount = int(input("Enter amount: "))
        balance = balance + amount
        print("Balance:", balance)

    elif choice == 3:
        amount = int(input("Enter amount: "))
        if amount <= balance:
            balance = balance - amount
            print("Balance:", balance)
        else:
            print("Insufficient balance")

    elif choice == 4:
        print("Thank you")
        break

    else:
        print("Invalid choice")



































    
