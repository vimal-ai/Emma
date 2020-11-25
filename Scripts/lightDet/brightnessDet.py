import imageio
import numpy as np
import cv2

f = imageio.get_reader('<video0>')





def img_estim(img, thrshld):
    is_light = np.mean(img) > thrshld
    return 'light' if is_light else 'dark'


print(img_estim(f, 127))

