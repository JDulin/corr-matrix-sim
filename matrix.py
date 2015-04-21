
import argparse
import csv
import numpy as np
import scipy as sp

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

def command():
    """ Parses command line argument - CSV file of eigenmodes. """
    parser = argparse.ArgumentParser(description="csv file of eigenmodes.")
    parser.add_argument('csvfile', metavar='file', type=str, 
                        help="File of a candidate topology's eigenmodes.")
    
    return parser.parse_args().csvfile

if __name__ == '__main__':
    print "Correlation computation in progress..."
    print command()

