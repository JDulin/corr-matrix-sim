"""
John Dulin
Case Western Reserve University
April 20, 2015
"""

import sys
import argparse
import numpy as np
import csv

def eigenmodes(args):
    """ Produces final csv file of eigenmode terms for correlation matrix computation. """
    filename = '%(eigenmodes)s_Top%(top)s.csv' % args
    print filename
    with open(filename, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ')
        writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

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
    eigenmodes(commands())
