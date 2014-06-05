numbers = []

def print_six(x, step):
    i = 0

    while i < x:
        #print "At the top i is %d" % i
        numbers.append(i)

        i += step
        #print "Numbers now: ", numbers
        #print "At the bottom i is %d" % i

print print_six(100, 20)

# rewrote script using for loop and range
printed_numbers = []

def print_numbers():
    for i in range(0,5,1):
        printed_numbers.append(i)
        print printed_numbers

print_numbers()