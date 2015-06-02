##  Correlation Matrix Simulation Tools

This repository contains two complementary tools for 
producing simulated correlation matrices of the 
CMB temperature anisotropy for a set of 
candidate oblique torus topologies:  

1)  An eigenmode generator for producing a csv file of 
the **k** wave vector values of the planar wave eigenmodes for a given 
topology, set of compactification lengths, and set of oblique angles.

2)  A mode-mode correlation matrix function which returns 
a 837 x 837 square matrix as a Numpy array from a given csv file of eigenmodes.

Together, these tools make a convenient workflow for computing reproducible 
mode-mode correlation matrices for cosmic topology searches using 
the correlation matrix of the Planck CMB.

##  Usage

The eigenmode production tool, eigenmodes.py, and 
the correlation matrix computation tool, matrix.py, are ran on the 
command line separately.  

First, run eigenmodes.py with the number of eigenmodes N you would like 
produced, the topology under consideration, three distance values (Lx, Ly, and Lz)
for the size of the fundamental domain (In units of Hubble length (4,228 Gpc).)
and three angle values for the slants of the oblique fundamental domain 
(In units of radians).  The candidate topologies are called by an index of numbers 
- 1 : Untwisted 3-torus
- 2 : Half-turn twisted 3-torus
- 3 : Quarter-turn twisted 3-torus
- 4 : Third-turn twisted hexagonal prism
- 5 : Sixth-turn twisted hexagonal prism

For example, to produce the first 200 eigenmodes of a quarter-turn 
space universe with sides of 1 Hubble Length and 3 slanted angles of 
0.5 radians (28.6 degrees), we would call:

`python eigenmodes.py 200 3 1 1 1 0.5 0.5 0.5`   .

This will output a space separated value file named

`200_Top3_1.0_1.0_1.0_0.5_0.5_0.5.csv`   ,

which is named by "N_TopI_Lx_Ly_Lz_A1_A2_A3" where I is the index of the topology.  
Note that the factor of 2*pi is removed from the **k** terms in this file 
and is added back in the correlation matrix.  
Each line of the file has the same format:

`n j xi_j kx ky kz`   .

So, each line of the file represents a planewave term of an eigenmode, indexed by 'j'.  
The matrix.py file reads each line of this to compute a  mode-mode correlation matrix.

##  Dependencies 

The only dependencies not in the Python standard library are the 
[Numpy and Scipy](http://www.scipy.org/install.html) libraries.  
Instructions for installing the entire 'Scipy stack' are through the link above.  

##  Notes and Issues



Some simple functions for writing and reading complex numbers to file are 
defined in complexIO.py for writing complex coefficients of eigenmode terms. 
Not all of them are used in eigenmodes.py as of early June 2015.

##  Acknowledgements  

This work is part of John Dulin's senior thesis project for the 
Case Western Reserve University Physics Department.  It was done 
under the tutelage of Prof. Glenn Starkman of the CWRU Physics Department 
and Institute for the Science of Origins, and with the 
assistance of Joshua Osborne to expand correlation matrix searches 
for cosmic topology to the cases of oblique torus topologies.  
