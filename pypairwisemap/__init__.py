from Bio.PDB import *
import numpy as np
import matplotlib.pyplot as plt
import os
import shutil

def make_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def remove_directory(directory):
    shutil.rmtree(directory)

def get_pairwise_matrix(pdb,chn,frg_beg,frg_end,atm):
    coords = []
    #file IO
    parser=PDBParser()
    PDBList().retrieve_pdb_file(pdb, pdir='pdb', file_format='pdb',obsolete=False)
    structure=parser.get_structure('X', './pdb/'+'pdb'+pdb+'.ent')
    remove_directory('./obsolete')
    #loop through structure
    for chain in structure.get_chains():
        if(chain.get_id()==chn):
            for atom in chain.get_atoms():
                if(atom.get_id()==atm):
                    coords.append(atom.get_coord())
    #initializing matrix
    pwmat = np.zeros((frg_end,frg_end), dtype='float')
    for row in range(0, frg_end):
        for col in range(0,frg_end):
            pwmat[row,col]=np.linalg.norm(coords[col]-coords[row])
    #return matrix
    return pwmat


def get_pairwise_matrix_plot(pdb,chn,frg_beg,frg_end,atm):
    make_directory('./plots/')
    mat = get_pairwise_matrix(pdb,chn,frg_beg,frg_end,atm)
    plt.matshow(mat)
    plt.savefig('./plots/'+pdb+'_'+str(frg_beg)+'_'+str(frg_end)+'_'+atm+'.png')
