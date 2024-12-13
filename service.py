# Simple dictionary of words to gesture mapping
sign_language_dict = {
    "hello": "gesture_hello.png",
    "thank you": "gesture_thank_you.png",
    "goodbye": "gesture_goodbye.png",
    # Add more gestures as needed
}

def get_sign_language_gesture(text):
    return sign_language_dict.get(text.lower(), "gesture_unknown.png")
