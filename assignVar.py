
import math
import random

# Python Sample : Assignment
# Version : Python 2.x
'''
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

print 'Python Assignment'
print 

# Numbers 
a = 2
b = 3
c = a + b
print 'c = ', c

d = 10
e = 3.0
f = d / e
print 'f = ', f

# Bitwise operation
g = 1
h = g << 2
print 'h = ', h

# Complex Numbers
k = 1 + 2j
l = 5 + 10j
m = k + l
print 'm = ', m

# Hex numbers
o = 0x0f
p = 0xef
q = o + p
print 'q = ', q

# Maths functions (need import math)
r = math.sin(100) + math.pi
s = abs(-100)
t = math.sqrt(4)
u = int(12.345)
v = round(10.123)
w = round(10.123, 2)
print 'r = ', r
print 's = ', s
print 't = ', t
print 'u = ', u
print 'v = ', v
print 'w = ', w

# random number (need import random)
x = random.random()
y = random.randint(1, 1000)
print 'x = ', x
print 'y = ', y


# String
z = 'This is a string.'
strlen = len(z)
print 'strlen = ', strlen

# String concatenation
s1 = 'abc'
s2 = 'def'
s3 = s1 + s2
print 's3 = ', s3

print '-'*40

# Swap string
s4 = 'Peter'
print 'swap s4 = ', s4[::-1]

# Strig conversion
s5 = "123"
n1 = int(s5) + 1
print "n1 = ", n1

# Character code 
s6 = 'a'
print 'Character code of s6 = ', ord(s6)
print 'Character of 97 = ', chr(97)

# Formating string
print "String formating %s, %d" % ("123", 456)

# String functions
s7 = "this is a test string."
print "capitalize : ", s7.capitalize()
print "center : ", s7.center(10)
print "isdigit : ", s7.isdigit()
print "substring = ", s7[5:7]










