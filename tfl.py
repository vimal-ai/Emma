import numpy as np
import tensorflow as tf
import cv2
import pathlib

# Load TFLite model and allocate tensors.
interpreter = tf.lite.Interpreter(model_path="/home/vimal/Projects/Emma/Models/CV/model.tflite")

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

interpreter.allocate_tensors()

# input details
print(input_details)
# output details
print(output_details)

#interpreter.allocate_tensors()

def draw_rect(image, box):
    y_min = int(max(1, (box[0] * 300)))
    x_min = int(max(1, (box[1] * 300)))
    y_max = int(min(300, (box[2] * 300)))
    x_max = int(min(300, (box[3] * 300)))

    # draw a rectangle on the image
    cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (255, 255, 255), 2)


# for file in pathlib.Path('/home/vimal/Projects/Emma/Data/').iterdir():
#     img = cv2.imread(r"{}".format(file.resolve()))
#     new_img = cv2.resize(img, (512, 512))
#
#     interpreter.set_tensor(input_details[0]['index'], [new_img])
#
#     interpreter.invoke()
#     rects = interpreter.get_tensor(
#         output_details[0]['index'])
#     scores = interpreter.get_tensor(
#         output_details[2]['index'])
#
#     print("For file {}".format(file.stem))
#     print("Rectangles are: {}".format(rects))
#     print("Scores are: {}".format(scores))

path = "/home/vimal/Projects/Emma/Data/img.jpg"
img = cv2.imread(path)
new_img = cv2.resize(img, (300, 300))

interpreter.set_tensor(input_details[0]['index'], [new_img])

interpreter.invoke()
rects = interpreter.get_tensor(
    output_details[0]['index'])

print(rects)

# scores = interpreter.get_tensor(
#     output_details[2]['index'])
#
# #print("For file {}".format(file.stem))
# #print("Rectangles are: {}".format(rects))
# #print("Scores are: {}".format(scores))
#
# for index, score in enumerate(scores[0]):
#     if score > 0.5:
#         print("Rectangles are: {}".format(rects[index]))
#         draw_rect(new_img, rects[0][index])
# cv2.imshow("image", new_img)
# cv2.waitKey(0)
