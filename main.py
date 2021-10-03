from random import choice

print("Enter the number of friends joining (including you):")
number = int(input())
if number <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    friends = {}
    names = []
    for i in range(number):
        names.append(str(input()))
    print("Enter the total bill value:")
    bill_first = int(input())
    bill = round(bill_first / number, 2)
    friends = dict.fromkeys(names, bill)
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    if str(input()) == "Yes":
        lucky = choice(names)
        print(lucky, "is the lucky one!")
        bill = round(bill_first / number - 1, 2)
        friends = dict.fromkeys(names, bill)
        friends[lucky] = 0
        print(friends)
    else:
        print("No one is going to be lucky")
        print(friends)
