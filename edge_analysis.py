import cv2
import numpy as np
from IPython.display import display
from PIL import Image

image = cv2.imread('images/image_4.jpeg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Canny
edges = cv2.Canny(gray, 50, 150, apertureSize=3)
# Harris
corners = cv2.cornerHarris(gray, 2, 3, 0.04)
# Threshold
image[corners > 0.04 * corners.max()] = [0, 0, 255]

# Line using Hough Transform
lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
if lines is not None:
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Circle using Hough Transform
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20,
                           param1=700, param2=50, minRadius=0, maxRadius=0)
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        cv2.circle(image, (i[0], i[1]), i[2], (255, 0, 0), 2)
        cv2.circle(image, (i[0], i[1]), 2, (0, 0, 255), 3)

# BGR image to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# OpenCV image to PIL format
pil_image = Image.fromarray(image_rgb)
pil_image.show()