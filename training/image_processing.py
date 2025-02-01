import cv2

cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

image = cv2.imread(r'C:\Computer Science\weed detection\testing\images\5.jpg')

if image is None:
    print("Error: Could not load image.")
else:
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()