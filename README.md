# Face Detection and Face Tracking System

This project is a real-time **Face Detection and Face Tracking System** built using **Python, OpenCV, and Raspberry Pi Pico**.  
It detects human faces through the live camera feed and tracks their movement using motors controlled by the L298N motor driver.

---

## 🚀 Features
- Real-time face detection using **OpenCV**  
- Dynamic face tracking (left, right, up, down, diagonal)  
- Integration of **Raspberry Pi Pico + L298N Motor Driver**  
- Applications in **AI, IoT, Robotics, and Surveillance**  

---

## 🛠️ Components Required
- Raspberry Pi Pico  
- Breadboard  
- L298N Motor Driver Module  
- Two Metal Gear Motors  
- Jumper Wires  
- USB Cable  
- Power Supply  

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/Yadam1298/Face-Detection-and-Face-Tracking-System.git
cd Face-Detection-and-Face-Tracking-System
```

### 2. Install dependencies
```bash
pip install opencv-python
```

### 3. Connect Hardware

Connect Motor 1 and Motor 2 to OUT1 and OUT2 on L298N motor driver.

Connect power supply to L298N and ground to Raspberry Pi Pico.

Use jumper wires to connect input pins of L298N to Raspberry Pi Pico GPIO.

Connect the camera for real-time video capture.

### 4. Save the main.py

save the code in Raspberry Pi Pico board. Dont change the name only save as main.py

### 5. Run the project
```bash
python fdft.py
```

### Working Principle

- OpenCV detects faces using Haar Cascade Classifiers.
- The system calculates the position of the detected face in the frame.
- Based on face position, signals are sent to Raspberry Pi Pico.
- Pico drives the motors via L298N, moving the camera to track the face.

### Applications

- Smart Surveillance – auto-tracking intruders or visitors
- Robotics – human-aware robots with face-following capability
- Smart Devices – auto-tracking webcams / selfie cameras
- Home Automation – motion-aware interactive systems

### Author

Developed by Yadam Naga Venkata Naveen Kumar

[LinkedIn](https://www.linkedin.com/in/ynvnk/)

[My GitHub Profile](https://github.com/Yadam1298)
