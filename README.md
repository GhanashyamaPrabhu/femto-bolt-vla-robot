# Femto Bolt Vision-Language-Action (VLA) Robot Perception System

## Overview

This project implements a **Vision-Language-Action (VLA) robotic perception system** using the **Orbbec Femto Bolt 3D depth camera**.

The goal of the system is to enable a robot to **observe its environment, understand contextual information, reason about potential hazards, and communicate with humans through natural language warnings.**

The system integrates **computer vision, vision-language models, and speech synthesis** to allow a robot to explain what it sees and alert humans when potentially unsafe situations occur.

Example robot outputs:

* *“A person is standing near a car.”*
* *“Please be careful. There are many obstacles nearby.”*
* *“Warning. A person is approaching the vehicle.”*

This project demonstrates a foundational **embodied AI perception pipeline** similar to those used in **autonomous robots and intelligent vehicles.**

---

# System Architecture

The perception pipeline follows a **Vision-Language-Action framework**:

```
Orbbec Femto Bolt Camera
            ↓
RGB Image Capture (OpenCV)
            ↓
Vision-Language Model (BLIP)
            ↓
Scene Description Generation
            ↓
Safety Reasoning Logic
            ↓
Speech Synthesis (Robot Communication)
```

The robot continuously observes the environment and produces **natural language explanations of the scene.**

If certain safety conditions are detected, the robot generates **warnings for humans nearby.**

---

# Hardware Used

### Orbbec Femto Bolt

The **Femto Bolt** is a high-performance RGB-D depth camera designed for robotics and spatial perception.

Features:

* RGB camera
* Depth sensing
* 3D perception capability
* USB 3.0 interface
* Designed for robotics and AI applications

Official website:

https://www.orbbec.com/products/tof-camera/femto-bolt/

---

# Software Stack

This project uses the following technologies:

| Technology               | Purpose                             |
| ------------------------ | ----------------------------------- |
| Python                   | Core programming language           |
| OpenCV                   | Camera capture and image processing |
| PyTorch                  | Deep learning framework             |
| HuggingFace Transformers | Vision-language models              |
| BLIP                     | Scene caption generation            |
| pyttsx3                  | Text-to-speech robot communication  |
| Git                      | Version control                     |
| GitHub                   | Project hosting                     |

---

# Project Structure

```
femto-bolt-vla-robot
│
├── test_camera.py
├── yolo_detection.py
├── vla_reasoning.py
├── README.md
└── .gitignore
```

Description of files:

### test_camera.py

Simple script to verify that the **Femto Bolt RGB camera is working**.

Features:

* Captures video stream
* Displays camera feed
* Used to validate camera setup

---

### yolo_detection.py

Real-time **object detection** using YOLOv8.

Capabilities:

* Detects objects in real time
* Draws bounding boxes
* Identifies common objects such as:

```
person
car
chair
laptop
cup
```

---

### vla_reasoning.py

Main **Vision-Language reasoning module**.

The script performs:

1. Capturing camera frames
2. Generating scene captions using a vision-language model
3. Applying reasoning rules
4. Generating robot speech output

Example output:

```
Robot perception: a man standing near a car
Robot says: Warning. A person is near the vehicle.
```

---

# Installation

Clone the repository:

```
git clone https://github.com/GhanashyamaPrabhu/femto-bolt-vla-robot.git
cd femto-bolt-vla-robot
```

Create virtual environment:

```
python3 -m venv vla_env
source vla_env/bin/activate
```

Install dependencies:

```
pip install torch
pip install opencv-python
pip install transformers
pip install sentencepiece
pip install accelerate
pip install pyttsx3
pip install pillow
```

---

# Running the System

### Step 1 — Test camera

```
python test_camera.py
```

You should see the live camera feed.

---

### Step 2 — Run object detection

```
python yolo_detection.py
```

The system will detect objects in real time.

---

### Step 3 — Run Vision-Language reasoning

```
python vla_reasoning.py
```

The robot will begin describing the scene.

Example terminal output:

```
Robot perception: a person standing next to a car
Robot says: Warning. A person is near the vehicle.
```

---

# Example Robot Warnings

The system includes simple reasoning rules to detect potentially unsafe situations.

Example conditions:

| Condition                   | Robot Warning                   |
| --------------------------- | ------------------------------- |
| Person detected near car    | Warning: person near vehicle    |
| Multiple obstacles detected | Please be careful while driving |
| Crowded environment         | Warning: many obstacles nearby  |

---

# Future Improvements

This project can be significantly expanded with more advanced robotics capabilities.

Planned improvements:

### Depth-based distance estimation

Using the Femto Bolt depth sensor to measure:

```
person distance = 1.2 meters
```

This enables better safety warnings.

---

### Human tracking

Tracking motion across frames to detect:

```
person approaching vehicle
```

---

### Temporal reasoning

Allowing the robot to understand motion over time.

Example:

```
A person has been approaching the car for the last 4 seconds.
```

---

### Autonomous navigation integration

Integrating the perception system with:

* mobile robots
* autonomous vehicles
* delivery robots

---

# Applications

This system has applications in:

* autonomous vehicles
* warehouse robots
* assistive robotics
* safety monitoring systems
* human-robot interaction research

---

# Author

Ghanashyama Prabhu
NYU Tandon School of Engineering
M.S. Mechatronics and Robotics

GitHub:

https://github.com/GhanashyamaPrabhu

---

# License

This project is released under the MIT License.

---

# Acknowledgements

* Orbbec for the Femto Bolt depth camera
* HuggingFace for vision-language models
* PyTorch for the deep learning framework
