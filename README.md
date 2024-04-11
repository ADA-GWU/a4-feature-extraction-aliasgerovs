# CSCI 6527 – Introduction to Computer Vision
### Assignment 4: Feature Extraction

This repository contains solutions to the Assignment 4. The tasks involve edge and corner detection, line and circle detection through Hough Transform, active contours for object detection, and interest point detection using ORB.

---

### Table of Contents
- [Installation](#installation)
- [Usage](#usage)
  - [Task 1: Basic Feature Extraction](#task-1-basic-feature-extraction)
  - [Task 2: Active Contour](#task-2-active-contour)
  - [Task 3: Interest Points Detection](#task-3-interest-points-detection)

---

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/ADA-GWU/a4-feature-extraction-aliasgerovs.git
   cd a4-feature-extraction-aliasgerovs


2. **Environment Setup**
Ensure you have Python 3.8+ installed. Setup your environment using:
```
pip3 install -r requirements.txt
```

---

### Usage

#### Task 1: Basic Feature Extraction
This task involves edge detection, corner detection, and the detection of lines and circles using Hough Transforms.

- **Edge Detection**
  ```bash
  python3 edge_analysis.py
  ```

#### Task 2: Active Contour
This task uses the Active Contour (snakes) algorithm to detect object borders.

- **Active Contour Detection**
  ```bash
  python3 active_contour.py
  ```

#### Task 3: Interest Points Detection
Implements ORB (Oriented FAST and Rotated BRIEF) to detect and match features between two images of the same scene from different angles.

- **Interest Points Detection**
  ```bash
  python3 interest_points.py
  ```

---