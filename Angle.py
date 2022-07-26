#!/usr/bin/python
# This script takes coordinates of three atoms and obtains the angle between two chemical bonds.
# Title:	Angle.py
# Author:	Reza Hemmati
# Created	03/07/2018
#
# USAGE
#	Angle.py  x1,y1,z1  x2,y2,z2  x3,y3,z3
#
# This script is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This script is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#

import sys, os, math
import os.path
import time
from operator import sub

def dotproduct(v1, v2):
	"""Calculate the dotproduct between two vectors."""
	return sum((a * b) for a, b in zip(v1, v2))

def length(v):
	"""Return the length of a vector."""
	return math.sqrt(dotproduct(v, v))

def angle(v1, v2):
	"""Return the angle between two vectors."""
	return math.acos(dotproduct(v1, v2) / (length(v1) * length(v2))) * (180.0 / (math.pi))

if (len(sys.argv) < 4):
	"""Check the number of input arguments."""
	sys.stderr.write('Wrong number of arguments!\n')
	sys.stderr.write('3 required, %d found.\n' % (len(sys.argv) - 1))
	sys.stderr.write('Usage: %s 1st-point 2nd-point 3rd-point like: x,x,x  x,x,x  x,x,x\n' % str(sys.argv[0]))
	sys.exit(1)

a = sys.argv[1].split(',')
b = sys.argv[2].split(',')
c = sys.argv[3].split(',')

a = map(float, a)
b = map(float, b)
c = map(float, c)

vec1 = map(sub, a, b)
if length(vec1) == 0:
	sys.stderr.write('\nCannot calculate angle for vectors with length zero.\n')
	sys.exit(1)
#print (vec1)

vec2 = map(sub, c, b)
if length(vec2) == 0:
        sys.stderr.write('\nCannot calculate angle for vectors with length zero.\n')
        sys.exit(1)
#print (vec2)

theta = angle(vec1, vec2)

print ("\nTHE ANGLE BETWEEN THOSE CHEMICAL BONDS IS {} DEGREE.\n".format(theta))
#end of the file
