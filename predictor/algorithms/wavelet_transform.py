# _*_ coding: utf-8 _*_

"""
This module provides a way to cancel data noise using wavelet transform
"""

from __future__ import print_function
import math
import numpy as np


def haar_matrix(size):
    """Compute Haar Matrix $H_n$
    Given the order of n (Haar Matrix is always a n-by-n square matrix),
    note that $n = 2^k, k\in N$,
    output the corresponding Haar Matrix $H_n$
    Haar matrix $H_n$ can be derived from $H_{n/2}$
    and identity/unit matrix $I_{n/2}$ by the following equation:
    $H_n = [H_{n/2}\otimes[1,1], I_{n/2}\otimes[1,-1]]$ (1)
    """
    if size >= 2**14:
        print("The size of entry is too large, it may cause MEMORY ERROR!")
        quit()

    k = int(math.log(size, 2))

    # Initialize Haar matrix by $H_2$
    haar = np.matrix([[1, 1], [1, -1]])
    average_transformer = haar[0]
    detail_transformer = haar[1]

    # For given $n = 2^k$, do $k-1$ times' iteration in Equation (1)
    # the result yield is $H_n$
    for j in range(1, k):
        # In j-th iteration,  in the left side of (1),
        # set the values to $H_{2^j}$ and $I_{2^j}$
        # we can obtaion $H_{2^{j+1}$
        unit = np.identity(2**j)
        haar = np.concatenate((np.kron(haar, average_transformer),
                               np.kron(unit, detail_transformer)))
    return np.matrix(haar)


def haar_transform(n):
    """Calculate Haar transformation Matrix $H_n$
    Haar transformation matrix is derived by the corresponding Haar matrix
    with the operation of normalization row by row
    """
    haar_before = haar_matrix(n)
    haar_before_abs = np.absolute(haar_before)

    # Do the normalization row by row
    for i in range(n):
        haar_before[i] = haar_before[i] / (np.sum(haar_before_abs[i])**0.5)
    return haar_before


def haar_wavelet_denoise(signal, level, threshold):
    """
    Given the time-series signal (an array with length $n = 2^k, k\in N$),
    set the level and threshold of haar wavelet transform,
    output the denoised time-series signal.
    """
    signal = np.matrix(signal).T
    n = signal.size
    coef = []

    # Step 1: Decomposion
    # Perform the haar transformation from Level $1$ to Level $level$
    for i in range(level):
        # Obtain the haar transform matrix of level (i+1)
        H = haar_transform(n)
        temp = H * signal
        n = n / 2
        coef = temp[n:].T.tolist() + coef
        signal = temp[:n]
    coef = signal.T.tolist() + coef

    # Step 2: Threshold
    # Set the coefficient which is no larger than threshold to 0
    for j in range(len(coef)):
        coef[j] = [0 if abs(elem) <= threshold else elem for elem in coef[j]]

    # Step 3: Reconstruct
    new_signal = coef
    for k in range(level):
        n = n*2
        H_transpose = haar_transform(n).T
        new_signal[1] = new_signal[0] + new_signal[1]
        del new_signal[0]
        new_signal[0] = (H_transpose * (np.matrix(new_signal[0]).T)).T.tolist()[0]

    return new_signal[0]


def threshold_estimate(signal):
    """Given a signal, output the estimated finest threshold"""
    signal = np.matrix(signal).T
    n = signal.size
    H = haar_transform(n)
    temp = H * signal

    # Note that, after applying haar wavelet tranform,
    # we can obtain a list of coefficients with same length as signal
    # and the coefficients are divided into two parts:
    # average coefficients $A$ and detail coefficients $D$
    D = temp[n/2:].T.tolist()[0]

    # calculate the mean absolute deviation of detail coefficients in $D$
    mean = np.sum(D) / float(len(D))
    deviation_square = [(elem-mean)**2 for elem in D]
    median_absolute_deviation = np.sum(deviation_square)/float(len(deviation_square))

    # Finally, we can calculte the universal threshold by the equation as follows:
    # $\lamda^U = root(MAD/0.6745) * root(2*log_e{n})$
    _lamda = ((median_absolute_deviation/0.6745)*(2*math.log(n)))**0.5

    return round(_lamda, 1)
