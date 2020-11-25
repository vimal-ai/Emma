import numpy as np
import cv2

cap = cv2.VideoCapture(1)
def img_estim(frame, thrshld):
    #print(np.mean(frame))
    print("no")
    is_light = np.mean(frame) > thrshld
    print("prob")
    #cv2.imshow('frame', frame)

    return 'light is on' if is_light else 'dark'

def detect():
    while True:
        _, frame = cap.read()
        #print(img_estim(frame, 127))
        print(type(frame))

        color = (255,255,255)
        stroke = 2
        font = cv2.FONT_HERSHEY_SIMPLEX
        print("0")
        output = str(img_estim(frame, 50))
        print("oo")
        output1 = str(np.mean(frame))
        print(output)
        cv2.putText(frame,output+output1, (10,30), font, 1, color, stroke, cv2.LINE_AA)
        cv2.imshow('video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

def main():
    print("first")
    detect()

if __name__ == "__main__":
    main()
