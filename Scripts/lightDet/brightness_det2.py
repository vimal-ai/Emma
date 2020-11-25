import numpy as np
import cv2

cap = cv2.VideoCapture(2)
def img_estim(frame, thrshld):
    print(np.mean(frame))
    is_light = np.mean(frame) > thrshld
    cv2.imshow('frame', frame)

    return 'light is on' if is_light else 'dark'


frame = cv2.imread('lightRoom.jpg')
#print(img_estim(frame, 127))

color = (255,255,255)
stroke = 2
font = cv2.FONT_HERSHEY_SIMPLEX
output_ = str(img_estim(frame, 75))
output1 = str(np.mean(frame))
print(output_)
cv2.putText(frame,output_+output1, (10,30), font, 1, color, stroke, cv2.LINE_AA)
cv2.imshow('photo', frame)
cv2.waitKey(0)
