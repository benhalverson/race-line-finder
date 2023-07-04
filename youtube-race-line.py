import cv2
import numpy as np
import googleapiclient.discovery
import yolo

def detect_racing_lines(video_id):
    video_url = get_video_url(video_id)

    video = cv2.VideoCapture(video_url)
    model = yolo.YOLOv7()

    while True:
        ret, frame = video.read()

        if ret: 
            detections = model.detect(frame)

            for detection in detections:
                cv2.rectangle(frame, detection[0], detection[1], (0, 255, 0), 2)
            cv2.imshow("frame", frame)

            if dv2.waitKey(1) == ord("q"):
                break

    video.release()


def get_video_url(video_id):
  service = googleapiclient.discovery.build("youtube", "v3")

  video_info = service.videos().list(port="snippet,contentDetails,statistics").execute()

  video_url = video_info = video_info["items"][0]["contentDetails"]["embeddableDetails"]["url"]

  return video_url


if __name__ == "__main__":
    detect_racing_lines(video_id="fb2sGh1kRfM")