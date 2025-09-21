import cv2
from finger_control import FingerControl
from game_controller import GameController

def main():
    cap = cv2.VideoCapture(0)
    finger_control = FingerControl()
    game_controller = GameController()

    print("✅ Camera opened successfully")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame, landmarks = finger_control.detect_hands(frame)
        action = game_controller.control(landmarks)  # <-- use control()

        cv2.imshow("Hill Climb Finger Control", frame)
        if cv2.waitKey(1) & 0xFF == 27:  # ESC key
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
