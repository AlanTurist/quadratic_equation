import math

def pure(a, c):

    if (a > 0 and c > 0) or (a < 0 and c < 0):
        print('\n\tThe equation has no solutions..')

    else:
        y = (-c)/a
        x = math.sqrt(y)
        print('\n\tThe solutions of equation are:\n\n\tx_1,2 = +/-','{0:.2f}'.format(x))