import cv2

# Dictionary mapping text to ASL gesture video paths
asl_gestures = {
    "hello": r"C:\Users\saikiran.pudi\Downloads\5211959-uhd_3840_2160_25fps.mp4",  # Path to "hello" video
    "thank you": r""C:\Users\saikiran.pudi\Downloads\5211961-uhd_3840_2160_25fps.mp4"",
    "yes": r"C:\Users\saikiran.pudi\Downloads\yes.mp4",
    "no": r"C:\Users\saikiran.pudi\Downloads\no.mp4",
}

# Function to play the ASL video
def play_gesture_video(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Cannot open video file {video_path}")
        return
    
    print(f"Playing gesture video: {video_path}")
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("ASL Gesture", frame)  # Show the video
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to close the video window
            break

    cap.release()
    cv2.destroyAllWindows()

# Function to map text input to ASL gesture
def map_text_to_asl(text):
    text = text.lower().strip()  # Ensure case-insensitivity (e.g., "hello" or "Hello")
    if text in asl_gestures:
        video_path = asl_gestures[text]
        play_gesture_video(video_path)
    else:
        print(f"No ASL gesture available for: {text}")

# Main function
def main():
    print("ASL Gesture Mapper")
    # Automatically select "hello" and play the video for "hello"
    text_input = input("Enter a word to translate to ASL (e.g., hello): ").strip()
    print(f"Displaying video for: {text_input}")
    map_text_to_asl(text_input)

if __name__ == "__main__":
    main()
