# COLLATZ SEQUENCE

# lets create the collatz sequence, where if a number(n) is even: n // 2, and if n is odd: 3 * n + 1
def collatz(number):
    if (number == 1):
        print('Arrived at final number')
        return number
    elif (number < 0):
        print('Number has to be larger than 0')
    elif (number % 2 == 0):
        newCollatz = number // 2
        print('Collatz iteration = ', newCollatz)
        return newCollatz
    else:
        newCollatz = 3 * number + 1
        print('Collatz iteration = ', newCollatz)
        return newCollatz


# the users chosen number will be stored as a integer in this variable
userChoice = int(input('User Choice: '));


# create the loop that iterates on the chosen number till n is 1
def finalCollatz(userChoice):

    newNum = collatz(userChoice)

    while (newNum > 1):
        newNum = collatz(newNum)



# call the function
finalCollatz(userChoice)
