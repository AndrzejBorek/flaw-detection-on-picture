from xml.etree.ElementTree import tostring
import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread(
    'Path to file', 0)
img2 = cv2.imread(
    'Path to file ', 1)


ret, thresh1 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)


kernel = np.ones((5, 5), np.uint8)

opening = cv2.morphologyEx(thresh2, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)


# find the contours from the thresholded image
contours, hierarchy = cv2.findContours(
    closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# draw all contours

# calculate area of contours -- it returns number of pixels
area = 0
for i in range(len(contours)):
    area = area + cv2.contourArea(contours[i])
print("AREA:")
print(area)

image = cv2.drawContours(img2, contours, -1, (0, 255, 0), 2)

cnt = []
for i in range(len(contours)):
    cnt.append(contours[i])

M = []
for i in range(len(cnt)):
    M.append(cv2.moments(cnt[i]))

cx = []
cy = []

for i in range(len(M)):
    cx.append(M[i]['m10']/M[i]['m00'])
    cy.append(M[i]['m01']/M[i]['m00'])
    print("Contour number "+str(i))
    print("X coordinates of center of weight: ")
    print(cx[i])
    print("Y coordinates of center of weight:  ")
    print(cy[i])

plt.imshow(image)
plt.show()
