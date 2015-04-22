
import argparse
import csv
import numpy as np
import scipy as sp
from scipy import special

def gauss(N):
    """ 
    N - Number of eigenmodes
    Returns an N array of statistically-independent Gaussian random variables.
    """
    mu, sigma = 0, 0.1 # TODO: What are these for Planck CMB data?
    return np.random.normal(mu, sigma, N)

def plane_wave(k, x):
    """  Returns the plane wave value.  """
    return np.exp(1j*np.dot(k, x)) 

def sph_bessel(l, z):
    """
    Spherical Bessel function of the first kind. 
    Returns [derivative, value] for all orders up to and including 'n'.
    """
    return special.sph_jn(l, z)

def command():
    """ Parses command line argument - CSV file of eigenmodes. """
    parser = argparse.ArgumentParser(description="csv file of eigenmodes.")
    parser.add_argument('csvfile', metavar='file', type=str, 
                        help="File of a candidate topology's eigenmodes.")
    
    return parser.parse_args().csvfile

def reader(filename):
    """ Reads eigenmode csv file with line by line generator.  """
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            yield row

if __name__ == '__main__':
    print "Correlation computation in progress..."
    for row in reader(command()):
        print row

