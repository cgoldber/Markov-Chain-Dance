import cv2
import numpy as np
import glob

# get maximum dimensions
max_width = 0
max_height = 0
for filename in glob.glob('dancePics/*.jpg'):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    if width > max_width:
        max_width = width
    if height > max_height:
        max_height = height

img_array = []
for filename in glob.glob('dancePics/*.jpg'):
    img = cv2.imread(filename)

    # Calculate the padding needed to reach the maximum dimensions
    top_pad = (max_height - img.shape[0]) // 2
    bottom_pad = max_height - img.shape[0] - top_pad
    left_pad = (max_width - img.shape[1]) // 2
    right_pad = max_width - img.shape[1] - left_pad

    padded_img = cv2.copyMakeBorder(img, top_pad, bottom_pad, left_pad, right_pad, cv2.BORDER_CONSTANT, value=(255, 255, 255))
    height, width, layers = padded_img.shape
    img_array.append(padded_img)
 
out = cv2.VideoWriter('vids/markovDancer.avi',cv2.VideoWriter_fourcc(*'XVID'), 1, (max_width, max_height))

for img in img_array:
    out.write(img)
out.release()