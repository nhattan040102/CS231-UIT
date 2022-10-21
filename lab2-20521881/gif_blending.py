import cv2
import imageio

fg = cv2.imread('foreground.jpg')
fg = cv2.cvtColor(fg, cv2.COLOR_BGR2RGB)

mask = cv2.imread('mask.png', cv2.IMREAD_UNCHANGED)

# url = "https://cdnb.artstation.com/p/assets/images/images/005/731/017/original/david-bautista-fire.gif"

url = "https://media0.giphy.com/media/2vmiW6mcYgKst3QVDK/giphy.gif"

frames = imageio.mimread(imageio.core.urlopen(url).read(), '.gif')

#chuan hoa

fg_h, fg_w, fg_c = fg.shape
bg_h, bg_w, bg_c = frames[0].shape
top = int((bg_h-fg_h)/2)
left = int((bg_w-fg_w)/2)
bgs = [cv2.cvtColor(frame[0: 581, 0:430, 0:3], cv2.COLOR_BGR2RGB) for frame in frames]

print(bgs[0].shape)


#resize img
fg = cv2.resize(fg, (430,581))

# bgs = cv2.resize(frames, (430,581))

results = []
alpha = 0.5
for i in range(len(bgs)):
    result = fg.copy()
    result[mask[:,:,3] != 0] = alpha * result[mask[:,:,3] != 0]
    bgs[i][mask[:,:,3] == 0] = 0
    bgs[i][mask[:,:,3] != 0] = (1-alpha)*bgs[i][mask[:,:,3] != 0]
    result = result + bgs[i]
    results.append(result)


imageio.mimsave('result.gif', results)
