import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def shi_tomasi(file_path: str) -> np.array:
    """
    Corner detection based on shi_tomasi good features to track.
    
    :param file_path: A file path that points to a valid image. Assumed to be valid.
    :type file_path: str
    :return: A numpy intp (N, 1, 2) array of the corners, ranked by their confidence.
    :rtype: Any
    """
    img = cv.imread(file_path)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    corners = cv.goodFeaturesToTrack(gray, maxCorners= 25, qualityLevel=0.01, minDistance=50)
    corners= np.intp(corners)

    
    return corners

def test_corners(file_path: str) -> None:
    """
    Testing function built to plot using matplotlib the results of some corner tracking function. 
    
    :param file_path: The image to be tracked.
    :type file_path: str
    """
    img = cv.imread(file_path)
    corners = shi_tomasi(file_path)
    for corner in corners:
        x, y = corner.ravel()
        cv.circle(img, center= (x, y), radius= 5, color= 255, thickness= -1)

    plt.imshow(img)
    plt.show()
    cv.waitKey(0)