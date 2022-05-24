import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/AndrzejBorek/OneDrive - DTP/Pulpit/bullet_hole.jpg',0)

average_color_row = np.average(img, axis=0)
average_color = np.average(average_color_row, axis=0)
print(average_color)

ret,thresh1 = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,100,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
plt.imshow(thresh2,'gray'), plt.show()


# titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
# images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
# for i in range(6):
#     plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])

kernel = np.ones((5,5),np.uint8)

opening = cv2.morphologyEx(thresh2, cv2.MORPH_OPEN, kernel)
#gradient = cv2.morphologyEx(opening, cv2.MORPH_GRADIENT, kernel)
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
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



