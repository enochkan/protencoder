# protencoder
### Introduction
This is a Python utility to implement various encoding methods for protein structures including: pairwise mapping, 20-20 vector and one-hot encoding. 

**Note: ~~pypairwisemap~~ has been renamed to protencoder in 0.9**

#### Pairwise mapping

The method of encoding protein structures in terms of pairwise distances between alpha-carbons on the protein backbone was first implemented in the paper *Generative Modeling for Protein Structures*, which eliminates the need for generative models to learn translational and rotational symmetries.

To read more: [Generative Modeling for Protein Structures](https://papers.nips.cc/paper/7978-generative-modeling-for-protein-structures.pdf)

#### 20-20 vector

#### One-hot encoding

### Installation
```python
pip install protencoder==0.9
```

### Usage
```python
import protencoder as pe
#prints pairwise matrix
#arguments: pdb id, chain, fragment begin, fragment end, atom type
print(pe.get_pairwise_matrix('2ok6','A',1, 12,'CA'))
#saves pairwise matrix plot under './plots'
pe.get_pairwise_matrix_plot('2ok6','A',1, 12,'CA')
```

### Sample plot   
#### Pairwise mapping with (n>900)
![](./assets/2ok6_CA.png)
