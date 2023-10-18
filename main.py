# This is a sample Python script.
from math import nan, floor

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
smaller = 15
larger = 69

remainder = nan
quotient = nan
s_cur = smaller
l_cur = larger
s_coef = [1, 0]
t_coef = [0, 1]
i = 0
r_prev = nan
while remainder !=0:
    quotient = floor(l_cur / s_cur)
    r_prev = remainder
    remainder = l_cur % s_cur
    l_cur = s_cur
    s_cur = remainder
    s_coef.append(s_coef[0]-s_coef[1] * quotient)
    s_coef = s_coef[1:]
    t_coef.append(t_coef[0]-t_coef[1] * quotient)
    t_coef = t_coef[1:]
    st = str(i) + "\t"
    for v in [quotient, remainder, l_cur,s_cur,s_coef,t_coef]:
        st += str(v) + "\t"
    print(st)
    i+=1

gcd = r_prev
coeff = [t_coef[0],s_coef[0]]
print (f"gcd = {gcd}\tcoeff = {coeff[0]},{coeff[1]}")
print(smaller * coeff[0] + larger * coeff[1])
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
