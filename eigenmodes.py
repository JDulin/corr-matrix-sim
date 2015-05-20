"""
John Dulin
Case Western Reserve University
May 14, 2015
"""

import sys
import argparse
import numpy as np
import csv

##  Topology plane wave term functions.  Indexed by 'topologies' dict, produces a single plane wave indexed by j.  
##  Factor of 2pi removed from wave vector.  Must be added in matrix computation.  
##  Format of each file line is: [n, j, xi_nj, kx, ky, kz]
def three_torus(n, j, size, angles):  
    mode = np.array([n, n, n])
    T = np.array([ [0, 0, size[0]], 
            [size[1]*np.sin(angles[0]), 0, size[1]], 
                [size[2]*np.cos(angles[2])*np.sin(angles[1]), 
                size[2]*np.sin(angles[2])*np.sin(angles[1]), 
                size[2]*np.cos(angles[1])] ])
    k = np.dot(T, mode)
    coeff = 1
    return [n, j, coeff] + k.tolist()

def half_turn(n, j, size, angles):
    T = np.array([ [0, 0, size[0]], 
            [size[1]*np.sin(angles[0]), 0, size[1]], 
                [size[2]*np.cos(angles[2])*np.sin(angles[1]), 
                size[2]*np.sin(angles[2])*np.sin(angles[1]), 
                size[2]*np.cos(angles[1])] ])
    if j == 1:
        mode = np.array([n, n, n])
        coeff = 1/np.sqrt(2)
    elif j == 2:
        mode = np.array([-n, -n, n])
        coeff = 1/np.sqrt(2) * -1**mode[2]
    
    k = np.dot(T, mode)
    return [n, j, coeff] + k.tolist()

def quarter_turn(n, j, size, angles):
    mode = np.array([n, n, n])
    T = np.array([ [0, 0, size[0]], 
            [size[1]*np.sin(angles[0]), 0, size[1]], 
                [size[2]*np.cos(angles[2])*np.sin(angles[1]), 
                size[2]*np.sin(angles[2])*np.sin(angles[1]), 
                size[2]*np.cos(angles[1])] ])
    R = np.array([ [0, -1, 0],
                    [1, 0, 0],
                    [0, 0, 1] ])
    x = 1/2.0
    nz = mode[2]
    ## TODO: Numpy arrays must be homogenous - Line 70 returns a complex128 array.
    ## TODO: Complex output form for coeffs - '(1+0j)'.  Parens added.
    if j >= 1:
        coeff = x
        if j >= 2:
            coeff = np.complex128(x * j ** nz)
            if j >= 3:
                coeff = np.complex128(x * j ** (2*nz))
                if j == 4:
                    coeff = np.complex128(x * j ** (3*nz))

    k = np.dot(T, mode)  ## Translate
    k = np.dot(R, k)     ## Rotate 
    ##  T and R as defined do not commute because T includes the Lx, Ly, Lz dependencies of k.  
    ##  So, compute R(T(k)) to include the length dependencies in k before twisting.
    return [n, j, coeff] + k.tolist()

def third_turn():
    print "third turn"

def sixth_turn():
    print "Sixth turn"

topologies = {1 : three_torus, 
              2 : half_turn, 
              3 : quarter_turn,
              4 : third_turn, 
              5 : sixth_turn}

## TODO: right number of b modes?
bterms = {1:1, 2:2, 3:4, 4:3, 5:6}

def eigenmodes(args):
    filename = '%(eigenmodes)s_Top%(top)s_%(lx)s_%(ly)s_%(lz)s_%(ax)s_%(ay)s_%(az)s.csv' % args
    size = np.array([args['lx'], args['ly'], args['lz']])
    angles = np.array([args['ax'], args['ay'], args['az']])
    modes = args['eigenmodes']
    top = args['top']
    terms = bterms[top]
    
    with open(filename, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ')
        for n in xrange(1, modes+1):   ## Follow math convention - Index terms beginning with 1.
            for j in xrange(1, terms+1):
                planewave = topologies[top](n, j, size, angles)
                writer.writerow(planewave)
        
def commands():
    """  
    Parses command line arguments.  
    Accepts -- arguments of the form '(Eigenmodes) (Top 3) Lx Ly Lz Ax Ay Az.'  
    Returns 8 entry dictionary.
    """
    parser = argparse.ArgumentParser(description='Define candidate shape.')
    parser.add_argument('eigenmodes', metavar='N', type=int, 
                        help='Number of eigenmodes to produce.')
    parser.add_argument('top', metavar='T', type=int, 
                        help='Number topology to produce the eigenmodes for (See README for topology numbers).')
    parser.add_argument('lx', metavar='Lx', type=np.float64, 
                        help='Length of the topology in the x dimension.')
    parser.add_argument('ly', metavar='Ly', type=np.float64, 
                        help='Length of the topology in the y dimension.')
    parser.add_argument('lz', metavar='Lz', type=np.float64, 
                        help='Length of the topology in the z dimension.')
    parser.add_argument('ax', metavar='Ax', type=np.float64, 
                        help='Angle of shape obliqueness in the x direction in radians.')
    parser.add_argument('ay', metavar='Ay', type=np.float64, 
                        help='Angle of shape obliqueness in the y direction in radians.')
    parser.add_argument('az', metavar='Az', type=np.float64, 
                        help='Angle of shape obliqueness in the z direction in radians.')

    return vars(parser.parse_args())

if __name__ == '__main__':
    """  Run application. """
    print "Test in Progress"
    eigenmodes(commands())
    
