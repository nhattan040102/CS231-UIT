import numpy as np
from scipy import signal
import cv2
from matplotlib import pyplot as plt

def convolution(X, H):
   
    # get the horizontal and vertical size of X and H
    imageColumns = X.shape[1]
    imageRows = X.shape[0]
    kernelColumns = H.shape[1]
    kernelRows = H.shape[0]

    # calculate the horizontal and vertical size of Y (assume "full" convolution)
    newRows = imageRows + kernelRows - 1
    newColumns = imageColumns + kernelColumns - 1

    # create an empty output array
    Y = np.zeros((newRows,newColumns))


    # go over output locations
    for m in range(newRows):
       for n in range(newColumns):
            for i in range(kernelRows):
                for j in range(kernelColumns):
                   if (m+i < imageRows ) and (n+j < imageColumns):
                         Y[m,n] = Y[m,n] + H[i,j]*X[m+i,n+j]
                        
        # make sure kernel is within bounds

        # calculate the convolution sum

    return Y

def cross_corr(img, mask):
    max_row    = img.shape[0] - mask.shape[0] + 1
    max_col    = img.shape[1] - mask.shape[1] + 1

    output = np.zeros([max_row, max_col])

    for curr_row in range(0, max_row):
        for curr_col in range(0, max_col):
            for curr_mask_row in range(0, mask.shape[0]):
                for curr_mask_col in range(0, mask.shape[1]):
                    output[curr_row, curr_col] += img[curr_row + curr_mask_row, curr_col + curr_mask_col] * mask[curr_mask_row, curr_mask_col]
                    # print("(" + str(curr_row) + "," + str(curr_col)  + ")" + "=" + "(" + str(curr_row + curr_mask_row) + "," + str(curr_col + curr_mask_col)  + ")" + "+" + "(" + str(curr_mask_row) + "," + str(curr_mask_col)  + ")")
    return output



A = cv2.imread('lab3_20521881/9-ro.jpeg')
B = cv2.imread('lab3_20521881/template.png')

A_gray = cv2.cvtColor(A, cv2.COLOR_RGB2GRAY)
B_gray= cv2.cvtColor(B, cv2.COLOR_RGB2GRAY)

A_gray = A_gray  - A_gray.mean()
B_gray = B_gray  - B_gray.mean()
# res = cv2.matchTemplate(A_gray, B_gray)
res = signal.correlate2d(A_gray,B_gray)
# res = cross_corr(A_gray, B_gray)
print(res.shape)
print(A_gray.shape)
print(B_gray.shape)
# C = signal.correlate(A,B)


plt.imshow(res, cmap='gray')
plt.show()
# cv2.waitKey(0)

