import time, sys
waiting = 1
waitingIncreasing = True
try:    
    while True:
        print(' ' * waiting, end='')
        print('########')
        time.sleep(0.2)
        
        if waitingIncreasing:
            waiting = waiting + 1
            if waiting == 10:
                waitingIncreasing = False
        else:
            waiting = waiting - 1
            if waiting == 1:
                waitingIncreasing = True

except KeyboardInterrupt:
    sys.exit()
