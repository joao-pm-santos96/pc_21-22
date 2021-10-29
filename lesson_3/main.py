#!/usr/bin/env python3
"""
***DESCRIPTION***
"""

"""
IMPORTS
"""

"""
METADATA
"""
__author__ = 'Joao Santos'
__copyright__ = 'Copyright October2021'
__credits__ = ['Joao Santos']
__version__ = '1.0.0'
__maintainer__ = 'Joao Santos'
__email__ = 'joao.pm.santos96@gmail.com'
__status__ = 'Production'
# __license__ = 'GPL'

"""
TODO
"""

"""
CLASS DEFINITIONS
"""

"""
FUNCTIONS DEFINITIONS
"""
def update(mean1, var1, mean2, var2):
    new_mean = (mean1*var2 + mean2*var1) / (var1+var2)
    new_var = (var1*var2) / (var1+var2)
    return [new_mean, new_var]

def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]

"""
MAIN
"""
if __name__ == '__main__':
    pass