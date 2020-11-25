import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
#Load YOLO

weights_path = "/home/vimal/Projects/Emma_models/yolov3.weights"
cfg_path = "/home/vimal/Projects/Emma_models/yolov3.cfg"
coco_path = "/home/vimal/Projects/Emma_models/coco.names"
net =cv2.dnn.readNet(weights_path, cfg_path)
classes = []
with open(coco_path, "r") as f:
    classes = [line.strip() for line in f.readlines()]

layer_name = net.getLayerNames()
outputLayers = [layer_name[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0,255,size=(len(classes), 3))

#Loading image
starting_time = time.time()

def objectDetection():
    img_id = 0
    while True:
        #img = cv2.imread("img.png")
        ret, img = cap.read()
        img_id += 1
        # img = cv2.resize(img, None, fx=0.8, fy=0.8)
        height, width, channels = img.shape

        # detecting Image
        blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, False)

        # for b in blob:
        #    for n, img_blob in enumerate(b):
        #        cv2.imshow(str(n), img_blob)

        net.setInput(blob)
        outs = net.forward(outputLayers)
        # print(outs)

        class_ids = []
        confidences = []
        boxes = []
        # showing info on screen:
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                #if confidence > 0.2:
                    # Object Detected
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    # cv2.circle(img, (center_x,center_y), 10, (0, 255, 0), 2)

                    # Rectangle Co-Ordinates:
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    # cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        # print(len(boxes))
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        #indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.8, 0.3)
        #print(indexes)
        number_objects_detected = len(boxes)
        font = cv2.FONT_HERSHEY_DUPLEX
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                color = colors[i]
                print(label)
                #cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                #cv2.putText(img, label, (x, y + 30), font, 1, color, 1)
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                cv2.putText(img, label + " " + str(round(confidence, 2)), (x, y + 30), font, 1, color, 1)

        # Detecting Objects
        elapsed_time = time.time() - starting_time
        fps = img_id / elapsed_time
        cv2.putText(img, "FPS: " + str(round(fps, 2)), (10, 50), font, 1, (0, 0, 0), 1)
        cv2.imshow("Image", img)
        #cv2.imshow('image', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break

def main():
    objectDetection()

if __name__ == "__main__":
    main()
