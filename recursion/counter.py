from time import sleep

def countdown_recursive(n):
    if n==0:
        return
    else:
        print(n)
        sleep(2)
        countdown_recursive(n-1)

countdown_recursive(10)










"""
def countdown(n):
    while n > 0:
        print(n)
        n -= 1
        sleep(2)

countdown(10)
"""



