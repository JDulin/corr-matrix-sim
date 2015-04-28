"""
John Dulin
Case Western Reserve University
April 27, 2015
"""

import sys
import argparse
import numpy as np
import csv

# TODO: Oblique
def three_torus(n, j, size, angles):  
    mode = np.array([n, n, n])
    k = np.divide(mode, size)   
    if j == 1:
        return np.append([n, j, 1], k)
    elif j == 2:
        return np.append([n, j, 7], k)

def half_turn(n, j, size, angles):
    print "Half"

def quarter_turn(n, j, size, angles):
    print "half"

def third_turn():
    print "third turn"

def sixth_turn():
    print "Sixth turn"

topologies = {1 : three_torus, 
              2 : half_turn, 
              3 : quarter_turn,
              4 : third_turn, 
              5 : sixth_turn }

## TODO: right number of b modes?
bterms = {1:2, 2:2, 3:4, 4:3, 5:6}

def test_eigenmodes(args):
    filename = '%(eigenmodes)s_Top%(top)s_%(lx)s_%(ly)s_%(lz)s.csv' % args
    size = np.array([args['lx'], args['ly'], args['lz']])
    angles = np.array([args['ax'], args['ay'], args['az']])
    modes = args['eigenmodes']
    top = args['top']
    terms = bterms[top]
    
    with open(filename, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for mode in xrange(1, modes+1):
            for term in xrange(1, terms+1):
                ## TODO: Modulus eigenmodes? 
                writer.writerow(topologies[top](mode, term, size, angles))
        

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
                        help='Angle of shape obliqueness in the x direction.')
    parser.add_argument('ay', metavar='Ay', type=np.float64, 
                        help='Angle of shape obliqueness in the y direction.')
    parser.add_argument('az', metavar='Az', type=np.float64, 
                        help='Angle of shape obliqueness in the z direction.')

    return vars(parser.parse_args())

if __name__ == '__main__':
    """  Run application. """
    print "Test in Progress"
    test_eigenmodes(commands())
