import cv2

capture = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))

print(capture.isOpened())

while capture.isOpened():
  print('Capturing frame')
  
  ret, frame = capture.read()
  if ret == True:

    output.write(frame)
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  else:
    break
    
capture.release()
output.release()
cv2.destroyAllWindows()