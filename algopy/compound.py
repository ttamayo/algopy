"""
This file contains functions like

algopy.prod

that are not represented as a single node in the
computational graph, but are treated as a **compound**
function. I.e., tracing algopy.prod will result
in a CGraph with many successive multiplication operations.
"""

import numpy
from algopy import zeros, Function, UTPM

def prod(x, axis=None, dtype=None, out=None):
    """
    generic prod function
    """

    if axis != None or dtype != None or out != None:
        raise NotImplementedError('')

    elif isinstance(x, numpy.ndarray):
        return numpy.prod(x)

    elif isinstance(x, Function) or  isinstance(x, UTPM):
        y = zeros(1,dtype=x)
        y[0] = x[0]
        for xi in x[1:]:
            y[0] = y[0] * xi
        return y[0]

prod.__doc__ += numpy.prod.__doc__

