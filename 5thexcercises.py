import sys
def collatz(number):# function define with parameter number
    if number %2 == 0:# if number even proceed and divided by 2
        return number // 2
    elif number %2 == 1:# If number is odd proceed and divided by 3 + 1
       return 3 * number + 1

while True:# the main loop that keep calling the function collatz and entering and intenger
    enterNum = int(input())
    i = collatz(enterNum)
    print(i)# print the result
    if i == 1:# and exit the program if value return is equal to 1
        sys.exit()
