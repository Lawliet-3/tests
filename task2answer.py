import os
import cv2

# Set the path to the dataset directory
dataset_dir = 'test1/data'

# Set the path to the images and labels directories
image_dir = os.path.join(dataset_dir, 'images')
label_dir = os.path.join(dataset_dir, 'labels')

# Get the list of image files
image_files = os.listdir(image_dir)

# Loop over each image file
for image_file in image_files:
    # Check if the file is an image
    if not image_file.endswith('.jpg'):
        continue
    
    # Get the corresponding label file name
    label_file = image_file.replace('.jpg', '.txt')
    label_path = os.path.join(label_dir, label_file)

    # Check if the label file exists
    if not os.path.exists(label_path):
        continue

    # Read the image
    image_path = os.path.join(image_dir, image_file)
    image = cv2.imread(image_path)
    
    #image = cv2.resize(image, (300,300))

    # Read the labels from the label file
    with open(label_path, 'r') as file:
        lines = file.readlines()

    # Loop over each line in the label file
    for line in lines:
        # Split the line by spaces
        values = line.strip().split()

        # Extract the label and coordinates
        label = int(values[0])
        x_center, y_center, width, height = map(float, values[1:])

        # Calculate the top-left and bottom-right coordinates of the bounding box
        image_height, image_width, _ = image.shape
        x1 = int((x_center - width / 2) * image_width)
        y1 = int((y_center - height / 2) * image_height)
        x2 = int((x_center + width / 2) * image_width)
        y2 = int((y_center + height / 2) * image_height)

        # Draw the bounding box
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

        # Put the label on top of the bounding box
        cv2.putText(image, str(label), (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    # Display the image with bounding boxes
    cv2.imshow('Image with Bounding Boxes',image)
    cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()