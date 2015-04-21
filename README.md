##  Correlation Matrix Simulation Tools

This repository contains two complementary tools for 
producing simulated correlation matrices of the 
CMB temperature anisotropy for a set of 
candidate oblique torus topologies:  

1)  An eigenmode generator for producing a csv file of 
the **k** wavevector values of the planar wave eigenmodes for a given 
topology, set of compactification lengths, and set of oblique angles.

2)  A mode-mode correlation matrix function which returns 
a 837 x 837 square matrix as a Numpy array from a given csv file of eigenmodes.

Together, these tools make a convenient workflow for computing  
reproducible mode-mode correlation matrix for cosmic topology searches using 
the correlation matrix of the Planck CMB.

##  Installation

##  Dependencies 

##  Acknowledgements  

This work is part of John Dulin's senior thesis project for the 
Case Western Reserve University Physics Department.  It was done 
under the tutelage of Prof. Glenn Starkman of the CWRU Physics Department 
and Institute for the Science of Origins, and with the 
assistance of Joshua Osborne to expand correlation matrix searches 
for cosmic topology to the cases of oblique torus topologies.  
