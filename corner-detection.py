import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# load images and labels

def load_images_and_labels(image_paths, labels):
  images = []
  for path in image_paths:
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    images.append(image)
    
  return np.array(images), np.array(labels)

image_paths = ["./frames/frame_0000.png", "./frames/frame_0001.png", "./frames/frame_0095.png", "./frames/frame_3499.png"]
labels = [1, 1, 1, 0]

images, labels = load_images_and_labels(image_paths, labels)


# detect corners using harris corner detection
def detect_corners(images):
  corner_images = []
  for image in images:
    #detect corners
    corners = cv2.cornerHarris(image, 2, 3, 0.04)
    corners = cv2.dilate(corners, None)
    corner_images.append(corners)
  return np.array(corner_images)

corner_images = detect_corners(images)

# Flatten the corner images for classification
features = corner_images.reshape((corner_images.shape[0], -1))

# split the data into training an dtesting sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# train a classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# evaluate the classifier
print("Train accuracy: ", clf.score(X_train, y_train))
print("Test accuracy: ", clf.score(X_test, y_test))