# convert the video file to images

import cv2
vidcap = cv2.VideoCapture('input_vids/stock_vid_1.mp4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("input_frame_1/frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1
