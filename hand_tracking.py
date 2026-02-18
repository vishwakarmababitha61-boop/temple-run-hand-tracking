import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self):
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(max_num_hands=1)
        self.mp_draw = mp.solutions.drawing_utils

    def get_hand_position(self):
        success, img = self.cap.read()
        if not success:
            return "CENTER"

        img = cv2.flip(img, 1)
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        result = self.hands.process(rgb)

        move = "CENTER"

        if result.multi_hand_landmarks:
            for hand in result.multi_hand_landmarks:
                lm = hand.landmark[8]
                x = lm.x

                if x < 0.3:
                    move = "LEFT"
                elif x > 0.7:
                    move = "RIGHT"

                self.mp_draw.draw_landmarks(img, hand, self.mp_hands.HAND_CONNECTIONS)

        cv2.imshow("Camera", img)
        cv2.waitKey(1)

        return move
if __name__ == "__main__":
    tracker = HandTracker()

    while True:
        move = tracker.get_hand_position()
        print(move)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    tracker.cap.release()
    cv2.destroyAllWindows()
