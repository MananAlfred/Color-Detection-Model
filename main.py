import cv2
from PIL import Image
from util import get_limits

yellow = [0, 255,255]       # yellow in BGR colorspace

cap = cv2.VideoCapture(0)

while True:
  ret, frame = cap.read() 

  hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  lowerLimit, upperLimit = get_limits(color=yellow)
  
  mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)
  
  # Conversion done for calling boundary box
  mask_PIL = Image.fromarray(mask)
  bBox = mask_PIL.getbbox()
  
  if bBox is not None:
    x1, y1, x2, y2 = bBox
    cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 5)
  
  print(bBox)


  cv2.imshow('frame', frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()