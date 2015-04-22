"""
John Dulin
Case Western Reserve University
April 21, 2015
"""

import sys
import argparse
import numpy as np
import csv

def three_torus(lx, ly, lz, n):  
    b = 2
    for i in xrange(1, n):
        mode = np.array([i, i, i])
        size = np.array([lx, ly, lz])
        k = np.dot(np.pi, np.divide(mode, size))
        if i % 2 == 1:
            return np.append([ 1, (i % b)+1], k, 1)
        elif i % 2 == 0:
            return np.append([ 2, (i % b)+1], k, 1)


def half_turn():
    print "Half"

def quarter_turn():
    print "Quarter"

topologies = {1 : three_torus, 
                2: half_turn, 
                3: quarter_turn }

'''
def eigenmodes(args):
    """ Produces final csv file of eigenmode terms for correlation matrix computation. """
    filename = '%(eigenmodes)s_Top%(top)s_%(lx)s_%(ly)s_%(lz)s.csv' % args
    with open(filename, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        b = 2
        for i in xrange(args['eigenmodes'] * b): # TODO: Take modulus of wavemodes.
            writer.writerow([i+1, 1] + topologies[1](args['lx'], args['ly'], args['lz'], i).tolist())
'''

def test_eigenmodes(args):
    filename = '%(eigenmodes)s_Top%(top)s_%(lx)s_%(ly)s_%(lz)s.csv' % args
    with open(filename, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        b = 2  ## TODO: For arbitrary top
        for i in xrange(args['eigenmodes'] * b):
            print topologies[1](args['lx'], args['ly'], args['lz'], args['eigenmodes'])
            print args['eigenmodes']
            writer.writerow(topologies[1](args['lx'], args['ly'], args['lz'], args['eigenmodes']))

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
