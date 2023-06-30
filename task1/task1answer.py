import os
import cv2

data_dir = 'test1/data'

image_dir = os.path.join(data_dir, 'images')
label_dir = os.path.join(data_dir, 'labels')
image_file = os.listdir(image_dir)
label_file = os.listdir(label_dir)

missing_labels = [file for file in image_file if file.replace('.jpg', '.txt') not in label_file]

missing_images = [file for file in label_file if file.replace('.txt', '.jpg') not in image_file]

print("Missing Labels:")
for label in missing_labels:
    print(label)

print("\nMissing Images:")
for image in missing_images:
    print(image)
