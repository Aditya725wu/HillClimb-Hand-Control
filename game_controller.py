import pyautogui

class GameController:
    def __init__(self):
        self.prev_action = None
        self.action_counter = 0
        self.stable_action = "neutral"

    def fingers_up(self, landmarks):
        """Check which fingers are up (basic logic)."""
        fingers = []
        fingers.append(landmarks[4][0] > landmarks[3][0])   # Thumb
        fingers.append(landmarks[8][1] < landmarks[6][1])   # Index
        fingers.append(landmarks[12][1] < landmarks[10][1]) # Middle
        fingers.append(landmarks[16][1] < landmarks[14][1]) # Ring
        fingers.append(landmarks[20][1] < landmarks[18][1]) # Pinky
        return fingers

    def control(self, landmarks):
        action = "neutral"
        if landmarks:
            fingers = self.fingers_up(landmarks)

            if fingers[0] and not any(fingers[1:]):        # Thumb only
                action = "accelerate"
            elif fingers[1] and not fingers[0] and not any(fingers[2:]):  # Index only
                action = "brake"
            elif all(fingers):                             # All fingers
                action = "neutral"

        # Stability check (needs 5 frames same action)
        if action == self.prev_action:
            self.action_counter += 1
        else:
            self.action_counter = 0

        if self.action_counter >= 5:  # change only if stable
            if self.stable_action != action:
                self.stable_action = action
                print(f"👉 Action: {action}")

                if action == "accelerate":
                    pyautogui.keyDown("right")
                    pyautogui.keyUp("left")
                elif action == "brake":
                    pyautogui.keyDown("left")
                    pyautogui.keyUp("right")
                else:  # neutral
                    pyautogui.keyUp("right")
                    pyautogui.keyUp("left")

        self.prev_action = action
        return self.stable_action
