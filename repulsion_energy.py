# This script calculates the repulsion energy of a molecue in Hartree.
# Title:	repulsion_energy.py
# Author:	Reza Hemmati
# Created	01/05/2017
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

import sys, math
import numpy as np

# Conversion from radians to degrees and vice versa.
rad2deg = 180.0 / math.pi
deg2rad = math.pi / 180.0

# Cartesian indices
xyz = {'X': 0, 'Y': 1, 'Z': 2, 0: 'X', 1: 'Y', 2: 'Z'}

# Relative atomic masses of elements in atomic mass units (amu).
# X and X1 are dummy atoms.
atomic_masses = {	'H' : 1.00794, 'He': 4.00260, 'Li': 6.94100, 'Be': 9.01218, 'B' : 10.8110,
		 	'C' : 12.0107, 'N' : 14.0067, 'O' : 15.9994, 'F' : 18.9984, 'Ne': 20.1797,
		        'Na': 22.9898, 'Mg': 24.3050, 'Al': 26.9815, 'Si': 28.0855, 'P' : 30.9738,
			'S' : 32.0650, 'Cl': 35.4530, 'Ar': 39.9480, 'K' : 39.0983, 'Ca': 40.0780,
      			'Sc': 44.9559, 'Ti': 47.8670, 'V' : 50.9415, 'Cr': 51.9961, 'Mn': 54.9380,
	       		'Fe': 55.8450, 'Co': 58.9332, 'Ni': 58.6934, 'Cu': 63.5460, 'Zn': 65.4090,
		        'X' : 0.0, 'X1' : 0.0}


# Atomic number of elements.
atomic_znumber = {	'H' : 1, 'He': 2, 'Li': 3, 'Be': 4, 'B' : 5,
        		'C' : 6, 'N' : 7, 'O' : 8, 'F' : 9, 'Ne': 10,
          		'Na': 11, 'Mg': 12, 'Al': 13, 'Si': 14, 'P' : 15,
          		'S' : 16, 'Cl': 17, 'Ar': 18, 'K' : 19, 'Ca': 20,
          		'Sc': 21, 'Ti': 22, 'V' : 23, 'Cr': 24, 'Mn': 25,
          		'Fe': 26, 'Co': 27, 'Ni': 28, 'Cu': 29, 'Zn': 30,
          		'X' : 0.0, 'X1': 0.0}

# Input syntax and usage warnings
def get_input():
    if (not len(sys.argv) == 2):
        print('\nUsage: python3 binding.py XYZ_FILE\n')
        print('  XYZ_FILE: xyz file of target molecule\n')
        sys.exit()
    else:
        xyz_file_name = sys.argv[1]
        return xyz_file_name

# Calculate distance between two cartesian coordinates
def get_r12(coords1, coords2):
    r = 0.0
    for i in range(3):
        r += (coords2[i] - coords1[i]) ** 2
    d = round(math.sqrt(r), 8)
    return d


#*** CLASSES ***#
# molecule class for molecular data
class molecule:
    def __init__(self, xyz_file_name):
        self.xyz_file = xyz_file_name
        self.readxyz(self.xyz_file)

    def readxyz(self, xyz_file_name):
        xyzf = open(xyz_file_name, 'r')
        self.xyzarr = np.zeros([1, 3])
        self.atom_names = []
        if not xyzf.closed:
            # Read the first line to get the number of particles
            self.npart = int(xyzf.readline())
            # and next for title card
            title = xyzf.readline()
    
            # Make an N x 3 matrix of coordinates
            self.xyzarr = np.zeros([self.npart, 3])
            i = 0
            for line in xyzf:
                words = line.split()
                if (len(words) > 3):
                    self.atom_names.append(words[0])
                    self.xyzarr[i][0] = float(words[1])
                    self.xyzarr[i][1] = float(words[2])
                    self.xyzarr[i][2] = float(words[3])
                    i = i + 1
        return self.xyzarr, self.atom_names

    def dist_name(self, names):
    	name = self.atom_names
    	print (name)
    	print ('Number of atoms: %i\n' % (self.npart), end='')
    	self.R = []
    	for i in range(len(name)):
    		for j in range(i+1, len(name)):
    			self.R.append((name[i] + name[j]))
    	return self.R
    
    def distance_matrix(self, xyzarr):
        self.npart, ncoord = xyzarr.shape
        self.rvec = []
        self.dist_mat = np.zeros([self.npart, self.npart])
        for i in range(self.npart):
            for j in range(i+1, self.npart):
            	r = get_r12(xyzarr[i], xyzarr[j])
            	if r == 0:
            		sys.exit('Error in geometry! two atoms are at the same position.\n')
            	else:
            		self.rvec.append(r)
            		continue
        return self.rvec
# END OF THE CLASSES


def atomic_number(list_atoms):
		mul = []
		for i in range(len(list_atoms)):
			for j in range(i+1, len(list_atoms)):
				mul.append(atomic_znumber[list_atoms[i]] * atomic_znumber[list_atoms[j]])
		return mul


# Get input arguments
xyz_file = get_input()

# Read in xyz file
mol = molecule(xyz_file)

t = mol.distance_matrix(mol.readxyz(xyz_file)[0])

D = mol.dist_name(mol.readxyz(xyz_file)[1])

# Print the multiplication of Z numbers
at_list = mol.readxyz(xyz_file)[1]
#print (atomic_number(at_list))

Nu = 0
for i in range(len(D)):
	print (D[i] + ':', t[i], ' , Nucler Repulsion Energy is: %.8f\n' % (atomic_number(at_list)[i] / t[i]))
	Nu += atomic_number(at_list)[i] / t[i]

print ('Total Nuclear Repulsion Energy is: %.8f\n' % Nu)

# End of the file
