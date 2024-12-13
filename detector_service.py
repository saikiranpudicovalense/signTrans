import cv2
import mediapipe as mp

# MediaPipe setup for hand gesture detection
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

def detect_hand_gesture(image_path):
    # Load the image for the sign language gesture
    img = cv2.imread(image_path)
    
    # Open a webcam feed to display the gesture
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb_frame)
        
        if result.multi_hand_landmarks:
            for landmarks in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)
        
        # Display the gesture image overlaid on the webcam feed
        frame[100:frame.shape[0], 100:frame.shape[1]] = img  # Adjust size/position
        cv2.imshow("Hand Gesture Detection", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
