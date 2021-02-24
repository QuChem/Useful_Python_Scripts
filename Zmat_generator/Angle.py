#!/usr/bin/python

# This code calculates the angle between two chemical bonds.
# This code takes coordinates of three atoms and obtains the angle between two chemical bons.

import sys, os, math
import os.path
import time
from operator import sub

def dotproduct(v1, v2):
  return sum((a*b) for a, b in zip(v1, v2))

def length(v):
  return math.sqrt(dotproduct(v, v))

def angle(v1, v2):
  return math.acos(dotproduct(v1, v2) / (length(v1) * length(v2)))*(180.0/(math.pi))

if (len(sys.argv) < 4):
	sys.stderr.write('Wrong number of arguments!\n')
	sys.stderr.write('3 required, %d found.\n' % (len(sys.argv)-1))
	sys.stderr.write('Usage: %s 1st-point 2nd-point 3rd-point like: x,x,x  x,x,x  x,x,x\n' % str(sys.argv[0]))
	sys.exit(1)

a=sys.argv[1].split(',')
b=sys.argv[2].split(',')
c=sys.argv[3].split(',')

#a=map(int, a)

a=map(float, a)
b=map(float, b)
c=map(float, c)
#d=map(sum, zip(a,b))

vec1=map(sub, a, b)
if length(vec1) == 0:
        sys.stderr.write('\nCannot calculate angle for vectors with length zero\n')
        sys.exit(1)

vec2=map(sub, c, b)
if length(vec2) == 0:
        sys.stderr.write('\nCannot calculate angle for vectors with length zero\n')
        sys.exit(1)

theta=angle(vec1,vec2)
print ("\nTHE ANGLE BETWEEN THOSE CHEMICAL BONDS IS {} DEGREE.\n".format(theta))

