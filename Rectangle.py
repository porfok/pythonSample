# Python Sample : Rectangle.py
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

class Rectangle(object):
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.width * self.height

# Class Square inherit Class Rectangle with prpperty width = height
class Square(Rectangle):
    def __init__(self, s):
       self.side = s
       self.width = s
       self.height = s


print "Python Class deom"
print
r = Rectangle (2, 3)
print "area of rectangle ", r.width, "x", r.height, " = ", r.area()

s = Square(10)
print "area of square ", s.side , " = ", s.area()


