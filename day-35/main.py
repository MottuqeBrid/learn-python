# eals with for loop and while loop
# break statement
for i in range(1, 11):
    print(i)
    if i==5:
        break
else:
    print("Loop completed")


#  continue statement
for i in range(1, 11):
    if i==5:
        continue
    print(i)
else:
    print("Loop completed")

# if you use break statement in for loop or while loop else part will not be executed