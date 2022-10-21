import cv2

old_img = cv2.imread('image/img1.jpg')
new_img = cv2.imread('image/img1.jpg')

cur_img = old_img.copy()
h = old_img.shape[0]
for w in range(h):
    cur_img[:w, :, :] = new_img[h-w:, :, :]
    cur_img[w:, :, :] = old_img[:h-w, :, :]

    cv2.imshow("image", cur_img)
    cv2.waitKey(1)
