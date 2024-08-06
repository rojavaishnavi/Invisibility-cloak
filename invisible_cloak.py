import cv2
import numpy as np
import os

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Allow the camera to warm up
import time
time.sleep(2)

print("Please remove any black objects from the frame. Capturing background...")

# Capture the background frame
for i in range(30):
    ret, background = cap.read()
    if not ret:
        print("Failed to capture background")
        cap.release()
        exit()

# Flip the background frame
background = np.flip(background, axis=1)

print("Background captured. Now you can bring the black cloth into the frame.")

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')  
output_path = os.path.join(os.getcwd(), 'output.avi')
out = cv2.VideoWriter(output_path, fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

# Define the color range for black color
lower_bound = np.array([0, 0, 0])  # Lower bound for black color
upper_bound = np.array([180, 255, 50])  # Upper bound for black color

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Flip the frame
    frame = np.flip(frame, axis=1)
    
    # Resize the background if needed
    if frame.shape != background.shape:
        background = cv2.resize(background, (frame.shape[1], frame.shape[0]))
    
    # Convert the frame to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Create a mask to detect the color
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    
    # Remove noise from the mask
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))
    
    # Create an inverted mask
    mask_inv = cv2.bitwise_not(mask)
    
    # Segment the color part out of the frame using the mask
    res1 = cv2.bitwise_and(frame, frame, mask=mask_inv)
    
    # Segment the background part out using the mask
    res2 = cv2.bitwise_and(background, background, mask=mask)
    
    # Combine both results to get the final output
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)
    
    # Write the final output to the video file
    out.write(final_output)
    
    # Display the final output
    cv2.imshow('Invisibility Cloak', final_output)
    
    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam, video writer, and close all windows
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Video saved at: {output_path}")
