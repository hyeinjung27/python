# 실습2

def gugudan_even():
    i = 2
    while i < 10:
        for j in range(1,10):
            print("%d * %d = %d" % (i, j, i*j))
        i += 2
        
def gugudan_odd():
    i = 1
    while i < 10:
        for j in range(1,10):
            print("%d * %d = %d" % (i, j, i*j))
        i += 2

def gugudan_odd_or_even(num):
    if (num % 2 == 0):
        gugudan_even()
    else:
        gugudan_odd()

gugudan_odd_or_even(5)

# 실습3

def gugudan_upgrade(num):
    i = 0
    while i < num:
        i += 1
        for j in range(1, 10):
            print("%d * %d = %d" % (i, j, i*j))

gugudan_upgrade(6)