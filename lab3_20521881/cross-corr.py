import string
import numpy as np


def cross_corr(img, mask):
    max_row    = img.shape[0] - mask.shape[0] + 1
    max_col    = img.shape[1] - mask.shape[1] + 1

    output = np.zeros([max_row, max_col])

    for curr_row in range(0, max_row):
        for curr_col in range(0, max_col):
            for curr_mask_row in range(0, mask.shape[0]):
                for curr_mask_col in range(0, mask.shape[1]):
                    # output[curr_row, curr_col] += img[curr_row + curr_mask_row, curr_col + curr_mask_col] * mask[curr_mask_row, curr_mask_col]
                    print("(" + str(curr_row) + "," + str(curr_col)  + ")" + "=" + "(" + str(curr_row + curr_mask_row) + "," + str(curr_col + curr_mask_col)  + ")" + "+" + "(" + str(curr_mask_row) + "," + str(curr_mask_col)  + ")")
    return output


A = np.array([[1,1,1,1,3], [1,1,0,1,0],[0,0,1,0,1]])
B = np.array([[1,-3],[2,1]])


print(cross_corr(A,B))

# 1 1 1 1 3           1 -3
# 1 1 0 1 0           2 1
# 0 0 1 0 1

1 -3 + 1