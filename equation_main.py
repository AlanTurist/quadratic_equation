#!/usr/bin/env python
# coding: utf-8

import solution_equation
import pure_equation
import spur_equation
import os
import sys

a = float(input("\nInsert a: "))
b = float(input("\nInsert b: "))
c = float(input("\nInsert c: "))

print('\n')
print('*'*25,'Solutions','*'*25)

if b == 0:
    pure_equation.pure(a, c)

elif c == 0:
    spur_equation.spur(a, b)

else:
    solution_equation.solution(a, b, c)

print('\n')
print('*'*60)

restart = input("\n\nIf you want to retry press 'Y' and 'enter'.\n\nTo exit press 'enter': ")

if restart == "Y":
    os.execl(sys.executable, sys.executable, * sys.argv) 
else:
    print("\nExit..")
    sys.exit(0)
