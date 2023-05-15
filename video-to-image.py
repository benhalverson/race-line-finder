import cv2

# load the video
video = cv2.VideoCapture("GX010180.MP4")

# get the total number of frames
frame_number = 0

while True:
  success, frame = video.read()

  if success:
    cv2.imwrite(f'frame_{frame_number:04d}.png', frame)
    frame_number += 1
  else:
    # no more frames
    break

print("Total frames: ", frame_number)
video.release()

print("Done!")