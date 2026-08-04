'''
Usage of else with for the else keyword will only be executed when the loop is completely done without any break


work_log = [0,1,1,1,0,1,0]
#result variable --> longest_streak
longest_streak = 0
current_streak = 0
for day in work_log:
    if day == 1:
        #print(day)
        current_streak = current_streak + 1
        if current_streak > longest_streak:
            longest_streak = current_streak
    else:
        current_streak = 0 #streak breaks
else:
    print(f'Longest Streak is {longest_streak}')
print("Execution done")

#In this case when the entire loop execution is done we get result of
#else block

work_log = [0,1,1,1,0,1,0]
#result variable --> longest_streak
longest_streak = 0
current_streak = 0
for day in work_log:
    if day == 1:
        #print(day)
        current_streak = current_streak + 1
        if current_streak > longest_streak:
            longest_streak = current_streak
    else:
        current_streak = 0 #streak breaks
else:
    print(f'Longest Streak is {longest_streak}')
print("Execution done")

#for-else with notifications scenario

#notifications = [0,0,0,0]
#try to take notifications from user --> list of integers
notifications = list(map(int,input("Enter the values --> 0 or 1:").split(',')))
print(notifications)
for notification in notifications:
    if notification == 1:
        print('Unread Notification')
        break
else:
    print('All Caught Up')

#try to make notifications from user --> list of integers
'''
#while -->it relies on condition, it will be completely exceuted until the
#condition is satisified....

'''
Syntax while:

while <condition>:
    statements(s).....
    ........
    ........


while True:
    print("Yes")

#It runs an infinite loop we need to press Ctrl+C (keyboard interrupt)

i = 0 #initialised statement
while i<=10:
    print(i)
    i=i+1 #counter


i = 0
while i<=10:
    print(10-1)
    i = i+1
'''

#banking scenario --> PIN authentication if more than 3 attempts
#Account locked..

pin ="2612"
max_attempts = 3
current_attempt = 0
while current_attempt <= max_attempts:
    entered_pin = input("Enter the ATM PIN:")
    if  entered_pin == pin:
        print("Login Successful")
        break
        #continue #it holds for this condition and skips to the next part o
    else:
        print("Entered PIN is wrong..Try again carefully")
        current_attempt +=1
else:
    print("Account Locked,try after 24hours....") 




























































