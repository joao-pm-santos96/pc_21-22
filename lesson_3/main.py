#!/usr/bin/env python3
"""
***DESCRIPTION***
"""

"""
IMPORTS
"""
import random
from typing import ValuesView

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

def buildNoise(mu, sigma):
    return random.gauss(mu, sigma)

def kalmanFilter(prev_nu, prev_covariance, measurement):

    A_t = 1
    R_t = 0
    C_t = 1
    Q_t = noise_covariance

    # Prediction
    propagated_value = A_t * prev_nu
    propagated_variance = A_t * prev_covariance * A_t + R_t

    # Correction
    kalman_gain = (propagated_variance * C_t)/(C_t * propagated_variance * C_t + Q_t)

    new_nu = propagated_value + kalman_gain * (measurement - C_t * propagated_value) 
    new_covariance = (1 - kalman_gain * C_t) * propagated_variance

    return [new_nu, new_covariance]
    
"""
MAIN
"""
noise_covariance = 1.666

if __name__ == '__main__':

    true_value = 5
    prev_nu = 0
    prev_covariance = true_value

    for _ in range(1000):
        noise = buildNoise(0, noise_covariance)
        measured_value = true_value + noise

        prev_nu, prev_covariance = kalmanFilter(prev_nu, prev_covariance, measured_value)

        print(str(prev_nu) + ' ' + str(prev_covariance))