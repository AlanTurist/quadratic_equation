#!/usr/bin/env python
# coding: utf-8

import solution_equation
import pure_equation
import spur_equation
import exept_def
import details_def
import os
import sys

a = float(input("\nInsert a: "))
b = float(input("\nInsert b: "))
c = float(input("\nInsert c: "))

D = ((b**2) - (4*a*c))

print('\n')
print('*'*25,'Solutions','*'*25)

detail = str(input("\nDo you want to see the detailed solution?\n\nFor yes press 'Y': "))

if detail == "Y":
    details_def.detail(a, b, c, D)
else:
    pass

if a == 0:
    exept_def.exeption(a, b, c)

elif b == 0 and c == 0:
    exept_def.exeption(a, b, c)

elif b == 0:
    pure_equation.pure(a, c)

elif c == 0:
    spur_equation.spur(a, b)

else:
    solution_equation.solution(a, b, c, D)

print('\n')
print('*'*61)

restart = input("\n\nIf you want to retry press 'Y' and 'enter'.\n\nTo exit press 'enter': ")

if restart == "Y":
    os.execl(sys.executable, sys.executable, * sys.argv) 
else:
    print("\nExit..")
    sys.exit(0)
