# COLLATZ SEQUENCE

def collatz(number):
    if (number == 1):
        print('Arrived at final number')
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


userChoice = int(input('User Choice: '));

def finalCollatz(userChoice):

    newNum = collatz(userChoice)

    while (newNum > 1):
        newNum = collatz(newNum)


finalCollatz(userChoice)
