# Vision-Voice-Object-Detector
A real-time object detection system that combines computer vision with voice feedback. The system uses YOLO (You Only Look Once) for object detection and provides audio descriptions of detected objects, including their counts and proximity to the center of the frame.

**Features**

- Real-time object detection using YOLO

- Audio feedback through text-to-speech

- Object counting and classification

- Nearest object detection

- Visual bounding boxes with confidence scores

- Customizable detection frequency

- Threading for smooth audio feedback


**Requirements**

- Python 3.x

- ultralytics

- OpenCV (cv2)

- pyttsx3

- YOLO model file ('your own model or model from the yolowebsite.pt')

Installation

<pre>
<code>pip install ultralytics opencv-python pyttsx3</code>
</pre>

**Usage**


- Place your YOLO model file (best.pt) in the project directory

**Run the script:**
<pre>
<code>python object_detector.py  
</pre>

**Configuration**

The script includes several configurable parameters:


- FPS_wait_counter: Adjusts the frequency of audio feedback (default: 15)

- video_source: Camera input source (default: 0 for primary camera)

- Speech rate and volume can be adjusted through the pyttsx3 engine properties


**How It Works**


- The system captures video input from the camera

- YOLO model processes each frame to detect objects

- Detected objects are counted and tracked

- The nearest object to the center is calculated

- Visual feedback is shown with bounding boxes and labels

- Audio feedback provides object counts and nearest object information

- Threading ensures smooth operation between vision and audio


**Future Improvements**

Add support for multiple camera sources

Implement object tracking

Add configuration file for easy parameter adjustment

Support for different YOLO models

Custom voice feedback templates


**License**

MIT License

**Contributing**

Contributions are welcome! Please feel free to submit a Pull Request.

