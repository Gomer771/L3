
import math
from math import pi, sqrt, tan, radians
print("Введите радиус круга в см")
a=input()
a=int(a)
pi=3.14
#находим длинну круга в см и м
print("длина круга", 2*pi*a ,"см,", (2*pi*a)/100, "м")
#находим площадь круга в см^2 и м^2
print("площадь круга", pi*a*a ,"см,", pi*a*a/10000, "м^2")
#найдём сторону описанного треугольника в см и м
print("сторона описанного треугольника", a*3**0.5*2,"см,", a*3**0.5*2/100 ,"м")
#найдём сторону описанного квадрата в см и м
print("сторона описанного квадрата", a*2,"см,", a**2/100 ,"м")
s = tan(radians(22.5))
#найдём сторону восьмиугольника
print("сторона", a*2,"см,", a**2/100 ,"м")