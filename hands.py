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
        print(
          f'Index finger tip coordinates: (',
          f'{hand_landmarks.landmark[8].x * image_width}, '
          f'{hand_landmarks.landmark[8].y * image_height})'
        )
        
        # drawing ur whole hand
        mp_drawing.draw_landmarks(
          image,
          hand_landmarks,
          mp_hands.HAND_CONNECTIONS,
          mp_drawing_styles.get_default_hand_landmarks_style(),
          mp_drawing_styles.get_default_hand_connections_style())
        
        # draws circle on finger tip
        cv2.circle(
          img = image,
          center = (int(hand_landmarks.landmark[8].x * image_width),int(hand_landmarks.landmark[8].y * image_height)),
          radius = 100,
          color = (70,190,190),
          thickness = 5
        )
        
        # draws random circles
        rect_pos = random.randint(100,400)
        rect_pt1 = None
        rect_pt2 = None
        
        rect_center = (int(hand_landmarks.landmark[8].x * image_width),int(hand_landmarks.landmark[8].y * image_height))
        
        if rect_center == rect_pos:
          cv2.rectangle(
            img = image,
            pt1 = (rect_pos+50, rect_pos-50),
            pt2 = (rect_pos-50, rect_pos+50),
            color = (190, 70, 70),
            thickness = -1
          )
        
        

    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))

    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()
