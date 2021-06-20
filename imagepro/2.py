import os, time
import numpy as np
import cv2 as c

while (1):

    src = c.imread("IMG_0601.JPG")
    img = c.resize(src, None, fx=0.4, fy=0.4)
    #img = src
    gray = c.cvtColor(img, c.COLOR_BGRA2GRAY)
    c.imshow("Test", img)
    c.imshow("Gray", gray)

    if c.waitKey(1) == 27:
        break
c.destroyAllWindows()

