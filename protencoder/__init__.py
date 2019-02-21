from Bio.PDB import *
import numpy as np
import matplotlib.pyplot as plt
import os
import shutil
import warnings
from Bio import BiopythonWarning
from Bio.SeqUtils import seq1
warnings.simplefilter('ignore', BiopythonWarning)

SEQMAP={
        'A':0,
        'C':1,
        'D':2,
        'E':3,
        'F':4,
        'G':5,
        'H':6,
        'I':7,
        'K':8,
        'L':9,
        'M':10,
        'N':11,
        'P':12,
        'Q':13,
        'R':14,
        'S':15,
        'T':16,
        'V':17,
        'W':18,
        'Y':19
    }

def make_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def remove_directory(directory):
    shutil.rmtree(directory)

def get_structure(pdb):
    #file IO
    parser=PDBParser()
    PDBList().retrieve_pdb_file(pdb, pdir='pdb', file_format='pdb',obsolete=False)
    structure=parser.get_structure('X', './pdb/'+'pdb'+pdb+'.ent')
    remove_directory('./obsolete')
    return structure[0]

def get_pairwise_matrix(pdb,chn,frg_beg,frg_end,atm):
    coords = []
    model = get_structure(pdb)
    #loop through structure
    chain = model[chn]
    for atom in chain.get_atoms():
        if(atom.get_id() == atm):
            coords.append(atom.get_coord())
    #initializing matrix
    if(len(coords) < frg_end):
        warnings.warn('fragment is larger than the number of residues')
        return None
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

def get_vector_encoding(pdb,chn,mut,pos,window):
    model = get_structure(pdb); res = []
    #loop through structure
    chain = model[chn]
    for residue in chain:
        if(residue.get_id()[1] == pos):
            try:
                for i in range(pos-window,pos+window+1):
                    res.append(chain[i].get_resname())
            except:
                warnings.warn('failed to generate matrix: window size exceeds given position')
    #encodes mutations as 20xpos vector
    res = [seq1(r) for r in res]
    res = [SEQMAP.get(r)for r in res]
    res = [20*idx+res[idx] for idx in range(0,len(res))]
    mut_vec = np.zeros(20*(2*window+1))
    for i in range(0,len(res)):
        if i is window:
            mut_vec[20*i+SEQMAP.get(mut)]=1
            mut_vec[res[i]]=-1
        else:
            mut_vec[res[i]]=1
    return mut_vec


print(get_vector_encoding('2ok6','A','M',84,3))