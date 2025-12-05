import random
a = random.randint(1, 10)
attempt = 4
i = 0
isWon = False
while i <= attempt:
    b = int(input("enter the number: "))
    if a == b:
        isWon = False
        break
    
    elif a < b:
        print("too high")
    else:
        print("too low")
    i += 1
print(f"the number is: ", {a})

if isWon == True:
    print("congratulation")
else:
    print("you lose try again")
