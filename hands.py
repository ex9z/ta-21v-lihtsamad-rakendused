# pip install mediapipe
# python.exe -m pip install opencv-python

from re import M
from turtle import color
import cv2
import mediapipe as mp
import random

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

left_hand_y = 0
left_hand_x = 0
right_hand_x = 0
right_hand_y = 0

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.3,
    min_tracking_confidence=0.7) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    image_height, image_width, _ = image.shape
    
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        # x,y pos of finger tip
        x = int(hand_landmarks.landmark[8].x * image_width)
        y = int(hand_landmarks.landmark[8].y * image_height)
        print(
          f'x:{x}, '
          f'y:{y}'
        )

        # left side of screen
        if x < 480/2:
          left_hand_y = y
          left_hand_x = x
          
        # right side of screen
        else:
          right_hand_y = y
          right_hand_x = x
        
        color = (190,20,0)
        
        cv2.circle(image, (left_hand_x,left_hand_y), 10, color, 2)
        cv2.rectangle(image,(20,left_hand_y),(20,left_hand_y+50), color,3)

        cv2.circle(image, (right_hand_x, right_hand_y), 10, color, 2)
        cv2.rectangle(image,(460,right_hand_y),(460,right_hand_y+50), color,3)
        
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))

    if cv2.waitKey(5) & 0xFF == 27:
      break

cap.release()