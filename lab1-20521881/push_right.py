import cv2

old_img = cv2.imread('image/img1.jpg')
new_img = cv2.imread('image/img1.jpg')

cur_img = old_img.copy()
w = old_img.shape[1]
for k in range(w):
    cur_img[:, :k, :] = new_img[:, w-k:, :]
    cur_img[:, k:, :] = old_img[:, :w-k, :]

    cv2.imshow("image", cur_img)
    cv2.waitKey(1)
