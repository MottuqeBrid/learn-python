# function arumala pass
def average(a=7, b=4):
    avg = (a + b) / 2
    print(f"The average of {a} and {b} is {avg}")

average(10, 20)
average(4)
average(b=14)


# multiple number average
def multi_avg(*numbers):
    # here numbers is a tuple
    sum = 0
    for i in numbers:
        sum=sum + i
    avg=sum/len(numbers)
    print(f"The average of {numbers} is {avg}")


multi_avg(2, 4, 6, 8, 10)

# return value from function
def square(n):
    return n * n

print(square(5))