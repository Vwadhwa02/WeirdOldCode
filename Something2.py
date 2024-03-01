import cv2
import numpy as np
from PIL import ImageGrab
import pyautogui

# Define a function to scroll up
def scroll_up():
    pyautogui.scroll(-100)

# Define a function to scroll down
def scroll_down():
    pyautogui.scroll(100)

# Define a function to track the eye movement
def track_eye_movement():
    # Capture the video feed from the webcam
    cap = cv2.VideoCapture(0)

    # Create a loop to continuously track the eye movement
    while True:
        # Read the next frame from the webcam
        ret, frame = cap.read()

        # Convert the frame to grayscale
        #ray = cv2.cvtColor(frame,cv2.COLOR_BAYER_BG2GRAY)

        # Detect the eyes in the frame
        eyes = cv2.CascadeClassifier('haarcascade_eye.xml').detectMultiScale(gray, 1.3, 5)

        # If at least one eye is detected
        if len(eyes) > 0:
            # Get the coordinates of the first eye
            eye = eyes[0]

            # Calculate the center of the eye
            center = (eye[0] + eye[2]) / 2, (eye[1] + eye[3]) / 2

            # If the center of the eye is above the middle of the screen, scroll up
            if center[1] < frame.shape[0] / 2:
                scroll_up()

            # If the center of the eye is below the middle of the screen, scroll down
            elif center[1] > frame.shape[0] / 2:
                scroll_down()

        # Display the frame
        cv2.imshow('Eye Movement Tracker', frame)

        # Wait for a key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam
    cap.release()

    # Close all windows
    cv2.destroyAllWindows()

# Start the eye movement tracker
track_eye_movement()