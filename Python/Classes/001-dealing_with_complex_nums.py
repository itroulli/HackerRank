# Name: Classes: Dealing with Complex Numbers
# Problem: https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem
# Score: 20

import math


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)

    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)

    def __mul__(self, no):
        return Complex(self.real * no.real - self.imaginary * no.imaginary,
                       self.imaginary * no.real + self.real * no.imaginary)

    def __truediv__(self, no):
        r = float(no.real ** 2 + no.imaginary ** 2)
        return Complex((self.real * no.real + self.imaginary * no.imaginary) / r,
                       (self.imaginary * no.real - self.real * no.imaginary) / r)

    def mod(self):
        return Complex(math.sqrt(self.real ** 2 + self.imaginary ** 2), 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % self.real
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % self.imaginary
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')

# OR, following a proposal in Discussions we can do these changes:
#
# def __str__(self) :
#     return '{0:.2f}{1:+.2f}i'.format(self.real, self.imaginary)
#
# print('\n'.join(map(str,[x+y, x-y, x*y, x/y, abs(x), abs(y)])))
