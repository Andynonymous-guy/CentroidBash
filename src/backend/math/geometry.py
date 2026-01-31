import numpy as np


def polygonate(corners: np.array) -> np.array:
    """
    Reorders points in corners with an arbitrarily selected starting point, clockwise,
    to form a polygon. 
    
    :param corners: A (N, 1, 2) numpy array of unsorted corners.
    :type corners: np.array
    :return: Sorted (N, 1, 2) numpy array of corners in clockwise winding order, polygon.
    :rtype: np.array
    """

    