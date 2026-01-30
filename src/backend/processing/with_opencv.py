import cv2 as cv
import numpy as np
from src.frontend.main import get_file
import matplotlib.pyplot as plt

img = cv.imread(get_file())
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

corners = cv.goodFeaturesToTrack(gray, maxCorners= 25, qualityLevel=0.01, minDistance=50)
corners= np.intp(corners)

for corner in corners:
    x, y = corner.ravel()
    cv.circle(img, center= (x, y), radius= 5, color= 255, thickness= -1)

plt.imshow(img),plt.show()
cv.waitKey(0)
