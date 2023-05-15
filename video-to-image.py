import os
import cv2

# Directory containing the videos
video_dir = 'videos'  # replace with your directory path

# Directory to save the frames
frame_dir = 'frames'  # replace with your directory path

# Get a list of all video files in the video directory
video_files = [f for f in os.listdir(video_dir) if f.endswith('.MP4')]

# Loop over all video files
for video_file in video_files:
    # Open the video file
    video = cv2.VideoCapture(os.path.join(video_dir, video_file))

    # Initialize frame counter
    frame_num = 0

    while True:
        # Read the next frame
        success, frame = video.read()

        # If the frame was read successfully, save it as a PNG image
        if success:
            cv2.imwrite(os.path.join(frame_dir, f'{video_file}_{frame_num:04d}.png'), frame)
            frame_num += 1
        else:
            # If no frame could be read, then we have reached the end of the video
            break

    # Release the video object
    video.release()

print("Processing of all videos completed.")