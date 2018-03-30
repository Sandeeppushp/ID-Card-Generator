import cv2
# change filename as your filename
img = cv2.imread('a.png')

color = [101, 52, 152] # 'cause purple!

# border widths; I set them all to 150
top, bottom, left, right = [30]*4

img_with_border = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)

lineThickness = 2
cv2.line(img_with_border,(0, 220), (1060, 220), (0,0,0),  lineThickness)
cv2.imwrite('a.png',img_with_border)
