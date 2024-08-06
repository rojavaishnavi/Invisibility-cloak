***Invisibility cloak***
 Invisibility cloak using opencv  Based on invisible clock of harry potter

***Credits***
This project was developed by Roja Vaishnavi.

This was a fun project created based a scene in Harry Potter Fictional Series.
The project demonstrates an "Invisibility Cloak" effect using computer vision techniques with OpenCV. The program captures a background frame and then replaces the black color in subsequent video frames with the background, creating the illusion of invisibility.

***Installation***
To run this program, you need to have Python and the following packages installed:

Install Python: Make sure Python is installed on your system. You can download it from python.org.

Install OpenCV:

You can install OpenCV using pip:
***code***
pip install opencv-python

Install NumPy:
You can install Numpy using pip:
***code***
pip install numpy


***How to Run***
To run the program, save the code in a file e.g., invisibility_cloak

***Clone the Repository***

Clone the repository to your local machine using the following command:
git clone https://github.com/yourusername/invisibility-cloak.git

cd invisibility-cloak

Run the Program:

python invisibility_cloak.py

#Steps and Code Explanation

1. Initialize Webcam and Capture Background.
Initialization: The webcam is initialized, and a short delay is added to allow the camera to warm up.
Background Capture: Several frames (default is 30) are captured to stabilize and store the background image. This ensures that the background image is clear and free from transient noise.

2. Define Color Range
Color Detection: The HSV color range for detecting the black color is defined. This range helps in creating a mask that identifies the black areas in the video frames.

***Color ranges for other colors***
#Blue
#lower_bound = np.array([100, 150, 0])
#upper_bound = np.array([140, 255, 255])

#Green
#lower_bound = np.array([40, 40, 40])
#upper_bound = np.array([80, 255, 255])

#Red
#lower_bound = np.array([0, 120, 70])
#upper_bound = np.array([10, 255, 255])
#or
#lower_bound = np.array([170, 120, 70])
#upper_bound = np.array([180, 255, 255])


3. Process Video Frames
Frame Capture: The program continuously captures frames from the webcam.
Frame Conversion: Each frame is converted from BGR to HSV color space for easier color detection.
Mask Creation: A mask is created to detect the black color within the specified range, and morphological transformations are applied to clean the mask.
Segmentation: The non-black parts of the frame are segmented using an inverted mask, while the black parts are replaced with the pre-captured background.
Combining Results: The segmented frame and background are combined to create the final output, giving the illusion of invisibility.

4. Output and Display
Video Writing: The processed frames are written to an output video file.
Display: The final output is displayed in a window, and the program terminates when the 'q' key is pressed.



