from utils.speech_to_text import recognize_speech
from services.translation_service import get_sign_language_gesture
from detector.detector_service import detect_hand_gesture
from src.utils.speech_to_text import recognize_speech
from src.services.translation_service import get_sign_language_gesture
from src.detector.detector_service import detect_hand_gesture
from utils.speech_to_text import recognize_speech
from src.utils.speech_to_text import recognize_speech
import sys
import os

# Add 'src' folder to the sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Now you can import modules from the 'src' directory
from utils.speech_to_text import recognize_speech





def main():
    # Step 1: Recognize speech and convert to text
    text = recognize_speech()
    
    if text:
        # Step 2: Map text to sign language gesture
        gesture_image = get_sign_language_gesture(text)
        print(f"Gesture image for '{text}': {gesture_image}")
        
        # Step 3: Display the corresponding hand gesture
        detect_hand_gesture(gesture_image)

if __name__ == "__main__":
    main()
