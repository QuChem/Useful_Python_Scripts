import os, math

def distance(atom1,atom2):
  xyz1=[float(x) for x in atom1.split(",")]
  xyz2=[float(x) for x in atom2.split(",")]
  return math.sqrt((xyz1[0]-xyz2[0])*(xyz1[0]-xyz2[0])
                  +(xyz1[1]-xyz2[1])*(xyz1[1]-xyz2[1])
                  +(xyz1[2]-xyz2[2])*(xyz1[2]-xyz2[2]))

lcart=[line.rstrip() for line in open("RS_cartesian.txt","r")]
lzmat=[line.rstrip() for line in open("zmat_to_fix","r")]
#print (lzmat)

latoms=[]
for s in lcart:
  k=s.split()
  latoms.append(k[1]+","+k[2]+","+k[3])

for i in range(len(lzmat)):
  k=lzmat[i].split()
  if len(k)==1:
    print (lzmat[i])
    continue
  at2=int(k[1])-1
  r=format(distance(latoms[i],latoms[at2]),"1.11f")
  k[2]=str(r)
  if len(k)==3:
    print (" ".join(k))
    continue
  at3=int(k[3])-1
  result=[line.rstrip() for line in os.popen("python Angle.py "+latoms[i]+" "+latoms[at2]+" "+latoms[at3])]
  for sr in result:
    if sr.find("ANGLE") != -1:
      angle=sr.split()[-2]
      break
  k[4]=str(angle)
  if len(k)==5:
    print (" ".join(k))
    continue
  at4=int(k[5])-1
  result=[line.rstrip() for line in os.popen("python Dihedral.py "+latoms[i]+" "+latoms[at2]+" "+latoms[at3]+" "+latoms[at4])]
  for sr in result:
    if sr.find("ANGLE")!=-1:
      dihedral=sr.split()[-2]
      break
  k[6]=str(dihedral)
  print (" ".join(k))
#os.system("rm -f zmat_fixer.py~")
#os.system("ls -ltr")

