import cv2

# loading image
image = cv2.imread('3.jpg')

# disp img
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()