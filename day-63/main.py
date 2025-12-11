# slake water gun Game


import random


def check(user, comp):
    if comp == user:
        return 0
    if (
        (user == 0 and comp == 2)
        or (user == 1 and comp == 0)
        or (user == 2 and comp == 1)
    ):
        return -1

    return 1


user = int(input("0 for snake, 1 for water, 2 for gun: "))
while user in [0, 1, 2]:

    comp = random.randint(0, 2)

    score = check(user, comp)
    print(
        f"Your choice: {"snake" if user == 0 else "water" if user == 1 else "gun" if user == 2 else "invalid"}"
    )
    print(
        f"Computer's choice: {"snake" if comp == 0 else "water" if comp == 1 else "gun" if comp == 2 else "invalid"}"
    )
    if score == 0:
        print("It's a tie")

    elif score == 1:
        print("You win")

    else:
        print("You lose")
    user = int(input("0 for snake, 1 for water, 2 for gun: "))
else:
    print("Invalid input! Game over.")
