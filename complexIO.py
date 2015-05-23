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
    raw = str(u) + '+' + str(v) + 'j'
    text.write(raw)

def read_number(text):
    """ Reads complex number from specified open file object at current index. 
    text - Open text file with mode 'r'
    """
    buff = list()
    for i in xrange(24):
        char = text.read(1)
        if char != 'j':
            buff.append(char)
        else:
            break
    ## TODO: Work for both '+' and '-'
    uvpair = ''.join(buff).split('+')
    return np.complex128(np.float64(uvpair[0]) + 1j * np.float64(uvpair[1]))

def texlex(z):
    z = np.complex128(z)
    return str(z).strip('(').strip(')')

def from_text(string):
    """ Converts a string complex to numpy.complex128. """
    ##  TODO:  This is all shit.  Pairs are split into a len(uvpair)==3 when there is a negative first number.
    if 'j' in string:
        uvpair = string.split('+')
        if len(uvpair) == 1:
            uvpair = string.split('-')
            if len(uvpair) == 1:
                return np.complex128(np.float64(string[:-1]))
        uvpair[-1] = uvpair[-1].strip('j')

        ##  TODO: '-' splits negative j's.
        ##  TODO: '' Doesn't cast to a float when a single digit number is split.
        if len(uvpair) == 3:
            uvpair = [uvpair[1], uvpair[2]]
        if uvpair[0] == '':
            uvpair[0] = 0
       
        print uvpair 
        return np.complex128(np.float64(uvpair[0]) + 1j * np.float64(uvpair[1]))
    else:
        return np.complex128(np.float64(string))

##  if __name__ == '__main__':
