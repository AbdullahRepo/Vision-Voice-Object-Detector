# Vision-Voice-Object-Detector 🎥 🔊

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![YOLO](https://img.shields.io/badge/YOLO-Supported-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A real-time object detection system that combines computer vision with voice feedback. The system uses YOLO (You Only Look Once) for object detection and provides audio descriptions of detected objects, including their counts and proximity to the center of the frame.

</div>

## ✨ Features

- 🔍 Real-time object detection using YOLO
- 🔊 Audio feedback through text-to-speech
- 🔢 Object counting and classification
- 📏 Nearest object detection
- 📦 Visual bounding boxes with confidence scores
- ⚙️ Customizable detection frequency
- 🧵 Threading for smooth audio feedback

## 🛠️ Requirements

- Python 3.x
- ultralytics
- OpenCV (cv2)
- pyttsx3
- YOLO model file ('your own model or model from the yolowebsite.pt')

## 📦 Installation

```bash
pip install ultralytics opencv-python pyttsx3
```

## 🚀 Usage

1. Place your YOLO model file (best.pt) in the project directory
2. Run the script:
```bash
python object_detector.py
```

## ⚙️ Configuration

The script includes several configurable parameters:

| Parameter | Description | Default Value |
|-----------|-------------|---------------|
| `FPS_wait_counter` | Adjusts the frequency of audio feedback | 15 |
| `video_source` | Camera input source | 0 (primary camera) |
| `speech_rate` | Text-to-speech speed | Configurable through pyttsx3 |
| `volume` | Audio output volume | Configurable through pyttsx3 |

## 🔄 How It Works

1. The system captures video input from the camera
2. YOLO model processes each frame to detect objects
3. Detected objects are counted and tracked
4. The nearest object to the center is calculated
5. Visual feedback is shown with bounding boxes and labels
6. Audio feedback provides object counts and nearest object information
7. Threading ensures smooth operation between vision and audio

## 🔮 Future Improvements

- [ ] Add support for multiple camera sources
- [ ] Implement object tracking
- [ ] Add configuration file for easy parameter adjustment
- [ ] Support for different YOLO models
- [ ] Custom voice feedback templates

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

If you have any questions or run into issues, please open an issue in the GitHub repository.

---
<div align="center">
Made with ❤️ for the Computer Vision community
</div>
