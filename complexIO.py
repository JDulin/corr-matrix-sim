"""
John Dulin
May 20, 2015
Complex number IO utilities

Some naive tools for writing complex numbers to file for cosmic topology research.
"""

import numpy as np

def write_number(z, text):
    """ Writes complex number out to specified open file object at current index.
    z - Complex number numpy.complex128
    text - Open text file with mode 'w'
    """
    u = np.real(z)
    v = np.imag(z)
    raw = str(u) + '+' + str(v) + 'i'
    text.write(raw)

def read_number(text):
    """ Reads complex number from specified open file object at current index. 
    text - Open text file with mode 'r'
    """
    buff = list()
    for i in xrange(24):
        char = text.read(1)
        if char != 'i':
            buff.append(char)
        else:
            break
    ## TODO: Work for both '+' and '-'
    uvpair = ''.join(buff).split('+')
    return np.complex128(np.float64(uvpair[0]) + 1j * np.float64(uvpair[1]))

def text_complex(z):
    return str(z).strip('(').strip(')').replace('j', 'i')

def from_text(ring):
    """ Converts a string complex to numpy.complex128. """
    ## TODO: Work for both '+' and '-'
    uvpair = ring.split('+')
    uvpair[1] = uvpair[1].strip('j').strip('i')
    return np.complex128(np.float64(uvpair[0]) + 1j * np.float64(uvpair[1]))
   
##  if __name__ == '__main__':
