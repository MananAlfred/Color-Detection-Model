🟡 Yellow Color Detector using OpenCV

This is a simple computer vision project that detects yellow-colored objects in real-time using a webcam. It's built using Python and the OpenCV (cv2) library — a great starting point for beginners exploring image processing and color detection.

🚀 Features
Detects yellow-colored objects in live video feed

Highlights the detected areas with contours or bounding boxes

Adjustable HSV range for yellow detection

🛠️ Requirements
Python 3.x

OpenCV (cv2)

Pillow 

Install OpenCV using pip if not already installed:

bash
Copy
Edit
pip install opencv-python

📸 How It Works
Captures video frames from the webcam

Converts each frame to HSV (Hue, Saturation, Value) color space

Applies a mask to isolate yellow colors

Draws contours around the detected yellow regions

▶️ How to Run
bash
Copy
Edit
python main.py
Make sure your webcam is connected. Press q to exit the window.

🧠 Customization
You can tweak the HSV range in the code to detect different shades of yellow or other colors.



Learning how color detection works using HSV space

Real-time image processing projects