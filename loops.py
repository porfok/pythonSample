# Python Sample : Loops 
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

# while lopp
print "Loop 1 demo"
a = 1
b = 10
while a < b:
    print "in while loop ", a
    a = a + 1
else:
    print "in else"


# pass
print
print "Loop 2 demo"
c = 1
d = 5
while c < d:
    print "in loop ", c
    c = c + 1
else:
    pass # do nothing

# break and continue
print
print "Loop 3 demo"
e = 0
f = 10
while e < f:
    e = e + 1
    if e == 5: break
    if e == 3: continue
    print "in loop ", e
else:
    print "in else"    


# for loop
print
print "For loop demo"
g = [1 , 2, 3, 4, 5, 6, 7]
for h in g:
    print "for loop element ", h

# for loop in range
print 
print "for loop in range demo"
i = range(10)
for j in i:
   print j    

# for loop in range 2
print 
print "for loop in range demo 2"
k = range(100, 110, 2)
for l in k:
   print l    


# read file
filename = open("loops.py")
for line in  filename:
    print line



