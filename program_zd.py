from xml.etree.ElementTree import tostring
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Pamietajcie żeby dać swoją ścieżkę - jeśli ścieżka do zdjęcia w folderze github/projekt wam nie zadziała
# pobierzcie zdjęcie np na pulpit i dajcie ścieżkę tam
img = cv2.imread(
    'C:/Users/AndrzejBorek/OneDrive - DTP/Pulpit/wood_texture4.jpg', 0)
img2 = cv2.imread(
    'C:/Users/AndrzejBorek/OneDrive - DTP/Pulpit/wood_texture4.jpg', 1)

# average_color_row = np.average(img, axis=0)
# average_color = np.average(average_color_row, axis=0)
# print(average_color)

ret, thresh1 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)


# titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
# images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
# for i in range(6):
#     plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])

kernel = np.ones((5, 5), np.uint8)

opening = cv2.morphologyEx(thresh2, cv2.MORPH_OPEN, kernel)
#gradient = cv2.morphologyEx(opening, cv2.MORPH_GRADIENT, kernel)
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

# -------- calculating number of pixels of defect 01.06 Andrzej
# area = cv2.countNonZero(closing)
# print(area)
# ---------


# plt.imshow(opening ,'gray')
# plt.show()
print("test")
# Initiate ORB detector
# orb = cv2.ORB_create()
# # find the keypoints with ORB
# kp = orb.detect(closing, None)
# # compute the descriptors with ORB
# kp, des = orb.compute(closing, kp)
# for i,keypoint in enumerate(kp):
#     print ("Keypoint %d: %s" % (i,keypoint.pt))
# # draw only keypoints location,not size and orientation
# img2 = cv2.drawKeypoints(closing, kp, None, color=(0, 255, 0), flags=0)
# plt.imshow(img2), plt.show()


# find the contours from the thresholded image
contours, hierarchy = cv2.findContours(
    closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# draw all contours

# calculate area of contours -- check what value that function returns
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

print(M[1]['m10']/M[1]['m00'])
print(M[1]['m01']/M[1]['m00'])

cx = []
cy = []

for i in range(len(M)):
    cx.append(M[i]['m10']/M[i]['m00'])
    cy.append(M[i]['m01']/M[i]['m00'])
    print("Kontur numer "+str(i))
    print("Współrzędne x środka ciężkości: ")
    print(cx[i])
    print("Współrzędne y środka ciężkości: ")
    print(cy[i])

plt.imshow(image)
plt.show()
