#!/usr/bin/python

# This code calculates the dihedral angle between chemical bonds.
# It takes coordinates of four atoms and gives the dihedral angle of chemical bonds.

import sys, os, math
import os.path
import time
from operator import sub

def dotproduct(v1, v2):
  return sum((a*b) for a, b in zip(v1, v2))

def cross(a, b):
    cross_p = [a[1] * b[2] - a[2] * b[1],
               a[2] * b[0] - a[0] * b[2],
               a[0] * b[1] - a[1] * b[0]]
    return cross_p

def length(v):
  return math.sqrt(dotproduct(v, v))

def angle(v1, v2):
  return math.acos(dotproduct(v1, v2) / (length(v1) * length(v2))) * (180.0 / math.pi)

if (len(sys.argv) < 5):
	sys.stderr.write('Wrong number of arguments!\n')
	sys.stderr.write('4 required, %d found.\n' % (len(sys.argv)-1))
	sys.stderr.write('Usage: %s 1st-point 2nd-point 3rd-point 4th-point like: x,x,x  x,x,x  x,x,x  x,x,x\n' % str(sys.argv[0]))
	sys.exit(1)

a=sys.argv[1].split(',')
b=sys.argv[2].split(',')
c=sys.argv[3].split(',')
d=sys.argv[4].split(',')

#a=map(int, a)

a=map(float, a)
b=map(float, b)
c=map(float, c)
d=map(float, d)
#d=map(sum, zip(a,b))

vec1=map(sub, b,a)
if length(vec1) == 0:
        sys.stderr.write('\nCannot calculate angle for vectors with length zero\n')
        sys.exit(1)

vec23=map(sub, c, b)
if length(vec23) == 0:
        sys.stderr.write('\nCannot calculate angle for vectors with length zero\n')
        sys.exit(1)

vec4=map(sub, d,c)
if length(vec4) == 0:
        sys.stderr.write('\nCannot calculate angle for vectors with length zero\n')
        sys.exit(1)

n1=cross(vec1, vec23)
l1=length(n1)
n1=[x/l1 for x in n1]

n2=cross(vec23, vec4)
l2=length(n2)
n2=[x/l2 for x in n2]

l23=length(vec23)
b2norm=[x/l23 for x in vec23]
m1=cross(n1,b2norm)

x=dotproduct(n1,n2)
y=dotproduct(m1,n2)

dihedral=math.atan2(y,x) * (180.0 / math.pi)
if dihedral>=0.0:
  dihedral=360.0 - dihedral
else:
  dihedral=-dihedral
print ("\nTHE DIHEDRAL ANGLE BETWEEN THOSE CHEMICAL BONDS IS {} DEGREE.\n".format(dihedral))

