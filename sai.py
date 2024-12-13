# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
# import cv2
# import requests

# # Initialize the Selenium WebDriver
# def initialize_driver():
#     driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and in PATH
#     driver.get("https://www.signasl.org/")
#     return driver

# # Search for a phrase on the website and fetch the video URL
# def search_asl(driver, phrase):
#     try:
#         # Find the search bar and enter the phrase
#         search_box = driver.find_element(By.NAME, "q")  # Adjust selector based on the website
#         search_box.clear()
#         search_box.send_keys(phrase)
#         search_box.send_keys(Keys.RETURN)
#         time.sleep(3)  # Wait for results to load

#         # Fetch the first video link (adjust as per website structure)
#         video_element = driver.find_element(By.CSS_SELECTOR, "video")  # Adjust selector
#         video_url = video_element.get_attribute("src")
#         return video_url
#     except Exception as e:
#         print(f"Error searching for ASL gesture: {e}")
#         return None

# # Download the video from the URL
# def download_video(video_url, save_path="asl_video.mp4"):
#     try:
#         response = requests.get(video_url, stream=True)
#         with open(save_path, "wb") as video_file:
#             for chunk in response.iter_content(chunk_size=1024):
#                 video_file.write(chunk)
#         print(f"Video downloaded to: {save_path}")
#         return save_path
#     except Exception as e:
#         print(f"Error downloading video: {e}")
#         return None

# # Play the downloaded video
# def play_video(video_path):
#     cap = cv2.VideoCapture(video_path)
#     if not cap.isOpened():
#         print(f"Error: Cannot open video file {video_path}")
#         return
    
#     print(f"Playing video: {video_path}")
#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             break
#         cv2.imshow("ASL Gesture", frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()

# # Main function to integrate all steps
# def main():
#     driver = initialize_driver()
#     phrase = input("Enter a word or phrase to translate into ASL: ").strip()
#     video_url = search_asl(driver, phrase)
#     if video_url:
#         video_path = download_video(video_url)
#         if video_path:
#             play_video(video_path)
#     else:
#         print("No video found for the given phrase.")
#     driver.quit()

# if __name__ == "__main__":
#     main()
# import time
# import cv2
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager

# def search_signasl(phrase):
#     # Setup Selenium WebDriver
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
#     chrome_options.add_argument("--disable-gpu")
#     chrome_options.add_argument("--no-sandbox")
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
#     try:
#         # Open SignASL website
#         driver.get("https://www.signasl.org/")
#         time.sleep(2)  # Allow page to load
        
#         # Find the search bar and enter the phrase
#         search_bar = driver.find_element(By.NAME, "q")  # 'q' is the name attribute of the search bar
#         search_bar.send_keys(phrase)
#         search_bar.send_keys(Keys.RETURN)
#         time.sleep(2)  # Wait for results
        
#         # Get the first video link
#         video_element = driver.find_element(By.CSS_SELECTOR, "video")
#         video_url = video_element.get_attribute("src")
        
#         if video_url:
#             print(f"Video URL found: {video_url}")
#             return video_url
#         else:
#             print("No video found for the given phrase.")
#             return None
#     except Exception as e:
#         print(f"Error: {e}")
#         return None
#     finally:
#         driver.quit()

# def play_video(video_url):
#     cap = cv2.VideoCapture(video_url)
#     if not cap.isOpened():
#         print(f"Error: Cannot open video from URL {video_url}")
#         return
    
#     print(f"Playing video from: {video_url}")
#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             break
#         cv2.imshow("ASL Gesture", frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to close the video window
#             break

#     cap.release()
#     cv2.destroyAllWindows()

# def main():
#     phrase = input("Enter a word or phrase to translate to ASL: ").strip()
#     video_url = search_signasl(phrase)
#     if video_url:
#         play_video(video_url)
#     else:
#         print("No video to display.")

# if __name__ == "__main__":
#     main()
# import requests
# from bs4 import BeautifulSoup
# import webbrowser

# # Base URL of the ASL website
# asl_website = "https://www.signasl.org/"

# # Function to search for a phrase on the ASL website
# def search_asl_phrase(phrase):
#     # Clean and prepare the search URL
#     search_url = f"{asl_website}search?query={phrase}"
#     print(f"Searching for: {phrase} on {search_url}")
    
#     try:
#         # Fetch the search page content
#         response = requests.get(search_url)
#         response.raise_for_status()  # Raise an exception for HTTP errors
        
#         # Parse the HTML content
#         soup = BeautifulSoup(response.text, 'html.parser')
        
#         # Find the first search result (assuming it links to a video page)
#         result_link = soup.find('a', class_="result-link")  # Update class or tag as per website structure
        
#         if result_link:
#             video_url = asl_website + result_link['href']  # Construct full URL for the video
#             print(f"Found video: {video_url}")
            
#             # Open the video in the default browser
#             webbrowser.open(video_url)
#         else:
#             print("No video found for the given phrase.")
    
#     except requests.RequestException as e:
#         print(f"An error occurred while searching: {e}")

# # Main function
# def main():
#     print("ASL Phrase Video Finder")
#     phrase = input("Enter a phrase to search for (e.g., hello): ").strip()
#     search_asl_phrase(phrase)

# if __name__ == "__main__":
#     main()
# import requests
# import webbrowser

# # Base URL of the ASL website
# asl_website = "https://www.signasl.org/sign/"

# # Function to search and display ASL phrase video
# def search_asl_phrase(phrase):
#     # Construct the URL for the specific sign
#     phrase_url = f"{asl_website}{phrase}"
#     print(f"Checking URL: {phrase_url}")
    
#     try:
#         # Check if the URL exists
#         response = requests.head(phrase_url)  # Use HEAD to check existence without downloading content
#         if response.status_code == 200:  # URL exists
#             print(f"Found video for '{phrase}': {phrase_url}")
#             webbrowser.open(phrase_url)  # Open the video in the default browser
#         else:
#             print(f"No video found for: {phrase}")
    
#     except requests.RequestException as e:
#         print(f"An error occurred while searching: {e}")

# # Main function
# def main():
#     print("ASL Phrase Video Finder")
#     phrase = input("Enter a phrase to search for (e.g., hello): ").strip().lower()
#     search_asl_phrase(phrase)

# if __name__ == "__main__":
#     main()

import requests
import webbrowser

# Base URL of the ASL website
asl_website = "https://www.signasl.org/sign/"

# Function to search and display ASL phrase video
def search_asl_phrase(phrase):
    # Replace spaces with hyphens for multi-word phrases
    formatted_phrase = phrase.replace(" ", "-")
    phrase_url = f"{asl_website}{formatted_phrase}"
    print(f"Checking URL: {phrase_url}")
    
    try:
        # Check if the URL exists
        response = requests.head(phrase_url)  # Use HEAD to check existence without downloading content
        if response.status_code == 200:  # URL exists
            print(f"Found video for '{phrase}': {phrase_url}")
            webbrowser.open(phrase_url)  # Open the video in the default browser
        else:
            print(f"No video found for: {phrase}")
    
    except requests.RequestException as e:
        print(f"An error occurred while searching: {e}")

# Main function
def main():
    print("ASL Phrase Video Finder")
    phrase = input("Enter a phrase to search for (e.g., hello, how are you): ").strip().lower()
    search_asl_phrase(phrase)

if __name__ == "__main__":
    main()