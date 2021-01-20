import cv2


img = cv2.imread('foto.jpg',1)
imgGray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)


# Filter Averaging
blur = cv2.blur(imgGray,(5,5))


# Filter Median
median = cv2.medianBlur(imgGray,5)




# Filtro Gaussian
gaussian = cv2.GaussianBlur(imgGray,(5,5),0)



cv2.imwrite('Averaging.jpg',blur)
cv2.imwrite('Median.jpg',median)
cv2.imwrite('Gaussian.jpg',gaussian)

cv2.imshow('Gray image',imgGray)
cv2.imshow('Averaging',blur)
cv2.imshow('Median',median)
cv2.imshow('Gaussian',gaussian)
cv2.waitKey()
cv2.destroyAllWindows()