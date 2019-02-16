# pypairwisemap
### Introduction
This is a Python utility to implement pairwise mapping of atomic spacing to represent protein structures in 2D. 

The method of encoding protein structures in terms of pairwise distances between alpha-carbons on the protein backbone was first implemented in the paper *Generative Modeling for Protein Structures*, which eliminates the need for generative models to learn translational and rotational symmetries.

To read more: [Generative Modeling for Protein Structures](https://papers.nips.cc/paper/7978-generative-modeling-for-protein-structures.pdf)

### Usage
```python
import pypairwisemap as pm
#prints pairwise matrix
#arguments: pdb id, chain, fragment begin, fragment end, atom type
print(pm.get_pairwise_matrix('2ok6','A',1, 12,'CA'))
#saves pairwise matrix plot under './plots'
pm.get_pairwise_matrix_plot('2ok6','A',1, 12,'CA')
```

### Sample plot   
![](./assets/2ok6_CA.png)
