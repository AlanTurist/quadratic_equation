#!/usr/bin/env python
# coding: utf-8

import solution_equation
import pure_equation
import spur_equation

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