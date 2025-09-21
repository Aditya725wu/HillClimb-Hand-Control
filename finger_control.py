# finger_control.py
import cv2
import mediapipe as mp

class FingerControl:
    def __init__(self,
                 max_num_hands=1,
                 min_detection_confidence=0.5,
                 min_tracking_confidence=0.5):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=max_num_hands,
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence
        )
        self.mp_draw = mp.solutions.drawing_utils

    def detect_hands(self, frame):
        """
        Input: BGR frame
        Output: frame (with drawings), landmarks list [(x,y),...21] or [] if none
        Landmarks are pixel coordinates (ints).
        """
        h, w, _ = frame.shape
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb)
        landmarks = []

        if results.multi_hand_landmarks:
            hand_landmarks = results.multi_hand_landmarks[0]  # use first hand
            self.mp_draw.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
            for lm in hand_landmarks.landmark:
                landmarks.append((int(lm.x * w), int(lm.y * h)))
        return frame, landmarks
