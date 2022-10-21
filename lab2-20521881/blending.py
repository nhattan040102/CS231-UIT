import cv2

fg = cv2.imread('foreground.jpg')

mask = cv2.imread('mask.png', cv2.IMREAD_UNCHANGED)

effect = cv2.imread('effect.jpg')

#resize img
effect = cv2.resize(effect, (430,581))
fg = cv2.resize(fg, (430,581))

# #change color of smoke effect
# effect[:,:,2] = 0


#Sao chép ảnh qua biến mới
result = fg.copy()
alpha = 0.5
for x in range(mask.shape[0]): # result.shape[0]: chiều cao ảnh
    for y in range(mask.shape[1]): # result.shape[1]: chiều rộng ảnh
        if (mask[x,y,3] != 0): # Kiểm tra điểm ảnh
            result[x,y] = (alpha * fg[x,y] + (1 - alpha) * effect[x,y])

cv2.imshow('Result', result)
cv2.waitKey(0)
