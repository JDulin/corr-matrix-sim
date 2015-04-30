
"""
John Dulin
Case Western Reserve University
April 27, 2015
"""

import argparse
import csv
import numpy as np
import scipy as sp
from scipy import special

def sph_bessel(ell, z):
    """
    Spherical Bessel function of the first kind. 
    Returns [derivative, value] for all orders up to and including 'n'.
    """
    return special.sph_jn(ell, z)

def plane_wave(k, x):
    return np.exp(1j*np.dot(k, x)) 

def command():
    """ Parses command line argument - CSV file of eigenmodes. """
    parser = argparse.ArgumentParser(description="csv file of eigenmodes.")
    parser.add_argument('csvfile', metavar='file', type=str, 
                        help="File of a candidate topology's eigenmodes.")
    
    return parser.parse_args().csvfile

def reader(filename):
    """ Reads eigenmode csv file with line by line generator.  """
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        for row in reader:
            yield row

if __name__ == '__main__':
    print "Correlation computation in progress..."
    for row in reader(command()):
        print row
