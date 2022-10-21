
import cv2

old_img = cv2.imread('image/img1.jpg')
new_img = cv2.imread('image/img1.jpg')
new_img[:, :, 0] = 255

cur_img = old_img.copy()
w = old_img.shape[1]
for k in range(0, w, 5):
    cur_img[:, w-k:, :] = new_img[:, :k, :]
    cur_img[:, :w-k, :] = old_img[:, :w-k, :]

    cv2.imshow("image", cur_img)
    cv2.waitKey(1)
