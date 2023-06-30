import cv2
import json
import time

# Load JSON data from file
with open('new_part2.json', 'r') as json_file:
    data = json.load(json_file)

# Open video file
video = cv2.VideoCapture('part2.mp4')

# Read the first frame
ret, frame = video.read()
height, width, _ = frame.shape

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_video = cv2.VideoWriter('output_video.mp4', fourcc, 30.0, (width, height))

# Iterate over frames
for frame_data in data:
    # Retrieve the frame ID
    frame_id = frame_data['frame_id']

    # Read the frame
    ret, frame = video.read()

    if not ret:
        break

    # Check if the frame contains track information
    if 'tracks' in frame_data:
        # Retrieve bounding box, track ID, and class ID for each person in the frame
        tracks = frame_data['tracks']
        for track in tracks:
            bbox = track['bbox']
            track_id = track['obj_id']
            class_id = track['class_id']

            # Draw bounding box
            x, y, w, h = bbox
            if class_id == 0:
                cv2.rectangle(frame, (x, y), (w, h), (0, 255, 0), 2)
            else: 
                cv2.rectangle(frame, (x, y), (w, h), (255, 0, 0), 2)

            # Define text label and color based on class ID
            label = "Adult" if class_id == 0 else "Kid"
            color = (0, 255, 0) if class_id == 0 else (255, 0, 0)

            # Add track ID and class label
            # cv2.putText(frame, f"Track ID: {track_id}", (x, y - 10), cv2.FONT_HERSHEY_DUPLEX, 0.7, color, 2)
            cv2.putText(frame, label + " : " + f" {track_id} ", (x, y - 40), cv2.FONT_HERSHEY_DUPLEX, 0.7, (255,255,255), 2)

    # Write the frame with bounding boxes, track IDs, and class labels to the output video
    output_video.write(frame)

    # Display the frame with bounding boxes, track IDs, and class labels
    cv2.imshow('Video', frame)
    
    time.sleep(0.003)
    
    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
video.release()
output_video.release()
cv2.destroyAllWindows()
