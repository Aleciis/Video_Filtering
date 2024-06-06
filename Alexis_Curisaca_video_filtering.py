import numpy as np
import cv2
import os
import math

cap = cv2.VideoCapture('MeAtTheZoo24FPS.mp4')
print(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(cap.get(cv2.CAP_PROP_FPS))
output="images"
i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break 
    frame_name = 'Frame'+str(i)+'.jpg'
    cv2.imwrite(os.path.join(output, frame_name), frame)
    i += 1


# BGR_copy=.copy()
# for r, row in enumerate(BGR_copy):
#     for c, value in enumerate(row):
       
#         value_0=value[0]
#         value_1=value[1]
#         value_2=value[2]
        
        
#         average_value=math.trunc((int(value_0) + int(value_1) + int(value_2))/ 3)
#         #print(average_value)
#         if  average_value > 128:
#            BGR_copy[r][c] = 255
#         else:
#            BGR_copy[r][c]=0
    
    




