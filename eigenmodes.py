"""
John Dulin
Case Western Reserve University
May 27, 2015
"""

import sys
import argparse
import numpy as np
import csv
import complexIO

class Topology:

    def __init__(self, size, angles, top, bterms):
        self.size = size
        self.angles = angles
        self.top = top  
        self.bterms = bterms
        ## Parallelepiped translation
        T = np.matrix([ [0, 0, size[0]], 
                    [size[1]*np.sin(angles[0]), 0, size[1]*np.cos(angles[0])], 
                    [size[2]*np.cos(angles[2])*np.sin(angles[1]), 
                    size[2]*np.sin(angles[2])*np.sin(angles[1]), 
                    size[2]*np.cos(angles[1])] ])
        ## Check to see if pseudo-inverse is necessary.
        if np.linalg.cond(T) < 1/sys.float_info.epsilon:
            # Define inverse
            self.Ti = T.I
        else:
            # Just define the identity
            self.Ti = np.identity(3)

    ##  Topology plane wave term functions.  Indexed by 'topologies' dict, produces a single plane wave indexed by j.  
    ##  Factor of 2pi removed from wave vector.  Must be added in matrix computation.  
    ##  Format of each file line is: [n, j, xi_nj, kx, ky, kz]
    def three_torus(self, n, j):  
        mode = np.array([[n], [n], [n]])
        k = np.dot(self.Ti, mode)
        coeff = 1
        return [n, j, coeff] + k.reshape((1,3)).tolist()[0]
    
    def half_turn(self, n, j):
        if j == 1:
            mode = np.array([[n], [n], [n]])
            coeff = 1/np.sqrt(2)
        elif j == 2:
            mode = np.array([[-n], [-n], [n]])
            coeff = 1/np.sqrt(2) * pow(-1, mode[2][0])
        
        k = np.dot(self.Ti, mode)
        return [n, j, coeff] + k.reshape((1,3)).tolist()[0]
    
    def quarter_turn(self, n, j):
        mode = np.array([[n], [n], [n]])
        R = np.matrix([ [0, -1, 0], 
                        [1, 0, 0], 
                        [0, 0, 1] ])
        x = 1/2.0
        nz = mode[2]
        k = np.dot(self.Ti, mode)  ## Translate
    
        ##  T and R as defined do not commute because T includes the Lx, Ly, Lz dependencies of k.  
        ##  So, compute R(T(k)) to include the length dependencies in Tk before twisting.
        ##  Rotate
        if j == 1:
            coeff = x
        if j == 2:
            coeff = np.complex128(x * ipower(nz))
            k = (R**3).dot(k)
        if j == 3:
            coeff = np.complex128(x * ipower(2*nz))
            k = (R**2).dot(k)
        if j == 4:
            coeff = np.complex128(x * ipower(3*nz))
            k = R.dot(k)
    
        coeff = complexIO.texlex(coeff) 
        return [n, j, coeff] + k.reshape((1,3)).tolist()[0]
    
    def third_turn(self, n, j):
        print "third turn"
    
    def sixth_turn(self, n, j):
        print "Sixth turn"

    space = {1 : three_torus, 
             2 : half_turn, 
             3 : quarter_turn,
             4 : third_turn, 
             5 : sixth_turn}

bterms = {1:1, 2:2, 3:4, 4:3, 5:6}

def eigenmodes(args):
    """  Produces the output file of eigenmodes, one term per line.  """
    filename = '%(eigenmodes)s_Top%(top)s_%(lx)s_%(ly)s_%(lz)s_%(ax)s_%(ay)s_%(az)s.csv' % args
    size = np.array([args['lx'], args['ly'], args['lz']])
    angles = np.array([args['ax'], args['ay'], args['az']])
    modes = args['eigenmodes']
    top = args['top']
    terms = bterms[top]
    
    shape = Topology(size, angles, top, terms)
    
    with open(filename, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ')
        for n in xrange(1, modes+1):   ## Follow math convention - Index terms beginning with 1.
            for j in xrange(1, terms+1):
                planewave = shape.space[top](shape, n, j)
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

def ipower(p):
    """ Computes a power of 'i' for the quarter turn space coeff. """
    if (p % 4) == 0:    
        return 1
    elif (p % 2) == 0:
        return -1
    elif (p % 2) == 1 and (p % 4) == 1:
        return 1j
    else: 
        return -1j

if __name__ == '__main__':
    """  Run application. """
    print "Test in Progress"
    eigenmodes(commands())
