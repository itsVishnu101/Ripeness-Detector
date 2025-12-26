import cv2
import numpy as np

def detect_ripeness(image_path):
    image = cv2.imread(image_path)
    if image is None:
        return "Unknown"

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # HSV ranges
    green_lower = np.array([35, 40, 40])
    green_upper = np.array([85, 255, 255])

    yellow_lower = np.array([20, 40, 40])
    yellow_upper = np.array([35, 255, 255])

    red_lower1 = np.array([0, 40, 40])
    red_upper1 = np.array([10, 255, 255])

    red_lower2 = np.array([170, 40, 40])
    red_upper2 = np.array([180, 255, 255])

    green_mask = cv2.inRange(hsv, green_lower, green_upper)
    yellow_mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
    red_mask1 = cv2.inRange(hsv, red_lower1, red_upper1)
    red_mask2 = cv2.inRange(hsv, red_lower2, red_upper2)
    red_mask = red_mask1 + red_mask2

    green_count = cv2.countNonZero(green_mask)
    yellow_count = cv2.countNonZero(yellow_mask)
    red_count = cv2.countNonZero(red_mask)

    if red_count > green_count and red_count > yellow_count:
        return "Ripe"
    elif yellow_count > green_count:
        return "Semi-Ripe"
    else:
        return "Unripe"
