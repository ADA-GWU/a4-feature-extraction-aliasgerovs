import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('images/image_5.jpeg', cv2.IMREAD_GRAYSCALE)  # Query image
img2 = cv2.imread('images/image_6.jpeg', cv2.IMREAD_GRAYSCALE)  # Train image
orb = cv2.ORB_create(nfeatures=1500)
keypoints1, descriptors1 = orb.detectAndCompute(img1, None)
keypoints2, descriptors2 = orb.detectAndCompute(img2, None)
matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = matcher.match(descriptors1, descriptors2)
matches = sorted(matches, key=lambda x: x.distance)
matched_image = cv2.drawMatches(img1, keypoints1, img2, keypoints2, matches[:50], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

plt.figure(figsize=(12, 6))
plt.imshow(matched_image)
plt.title('Top 50 matches between two images')
plt.show()