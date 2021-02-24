#!/usr/bin/python

import sys

def geomandcharge(filename):
   l = [line.rstrip() for line in open(filename, 'r')]
   ifound = 0
   done = 0
   charges = []
   geom = []
   for s in l:
      k = s.split()
      if done == 0:
        if ifound == 2:
          ifound = 3
          continue
        if ifound == 3 and len(k) <  6:
          done = 1
          continue
        if len(k) < 2:
          ifound = 1
          continue
        if k[0] == "NR" and k[1] == "ATOM":
          ifound = 2
          continue
        if ifound == 3:
          geom.append(" ".join(k[1])+": " + ", ".join(k[3:])+', ')
      else:
        if done == 1:
          if len(k) < 2:
            ifound = 4
            continue
          if k[0] == "Unique" and k[1] == "atom":
            ifound = 5
            continue
          if ifound == 5:
            charges.append("".join(k[-2:]))
   for (xyz, charge) in zip(geom, charges):
      print (' '+xyz+charge)
   return 1

name = sys.argv[1]

geomandcharge(name)

