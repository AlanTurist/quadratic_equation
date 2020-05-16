import math
import cmath

def solution(a, b, c):

    D = ((b**2) - (4*a*c))

    if D >= 0:
        disc = math.sqrt(D)
        x1 = (-b + disc)/(2*a)
        x2 = (-b - disc)/(2*a)
        print("\nThe solutions of equation are:\n\n\tx_1 = "'{0:.2f}'.format(x1),"\nand\n\n\tx_2 = "'{0:.2f}'.format(x2))

    else:
        print("\nThe equation has complex solutions..")
        disc = cmath.sqrt(D)
        x1 = (-b + disc)/(2*a)
        x2 = (-b - disc)/(2*a)
        print("\nThe solutions of equation are:\n\n\tx1 = "'{0:.2f}'.format(x1),"\nand\n\n\tx2 = "'{0:.2f}'.format(x2))
