import cv2
import numpy as np

gif = cv2.VideoCapture('lena_color.gif')
_, img = gif.read()
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

width, height = img.shape
print (img.dtype)
# print (img)
# Image.fromarray(img,'L')

# To change to other types, use img.astype(np.uint8) so calculations can go negative
img = img.astype(np.int16)

bmax = 0
bmin = 0

gradients = np.zeros((width, height))
for y in range(height):
    # We skip the last column hence the - 1
    for x in range(1, width - 1):
        gradients[x][y] = (img[x + 1][y]) - (img[x - 1][y])
        bmax = gradients[x][y] if gradients[x][y] > bmax else bmax
        bmin = gradients[x][y] if gradients[x][y] < bmin else bmin

print bmax, bmin

# img = (img - bmin)/abs(bmax - bmin) * 255
for y in range(height):
    # We skip the last column hence the - 1
    for x in range(1, width - 1):
        img[x][y] = (gradients[x][y] - bmin)/(bmax - bmin) * 255



img = img.astype(np.uint8)
cv2.imwrite('meow.jpg', img)
