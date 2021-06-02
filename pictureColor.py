import cv2
import numpy as np

img = cv2.imread("Resources/cat2.png")
kernel = np.ones((5, 5), np.uint8)

imGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imGray, (7, 7), 0)
imgCanny = cv2.Canny(img, 100, 150)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)
cv2.imshow("Original Image", img)
cv2.imshow("Gray Image", imGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dilation Image", imgDilation)
cv2.imshow("Eroded Image", imgEroded)

cv2.waitKey(0)
