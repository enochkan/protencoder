from Bio.PDB import *
import numpy as np

arg='2OK6'

dim = [0]
coords = [0]
parser=PDBParser()
PDBList().retrieve_pdb_file('2BEG', pdir='./')

structure=parser.get_structure('X', arg+'.pdb')

for chain in structure.get_chains():
    for atom in chain.get_atoms():
        #getting alpha carbon
        if(atom.get_id()=='CA'):
            dim.append(atom.get_serial_number())
            coords.append(atom.get_coord())

pwmat = np.zeros((len(dim), len(dim)), dtype='float')
#adding attributes
np.asarray(dim)
pwmat[0] = np.asarray(dim)
for row in range(1, len(dim)):
    pwmat[row,0]= dim[row]
    for col in range(1,len(dim)):
        pwmat[row,col]=np.linalg.norm(coords[col]-coords[row])

print(pwmat)
    