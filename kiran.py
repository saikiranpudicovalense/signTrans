# import requests
# import webbrowser

# # Base URL of the ASL website
# asl_website = "https://www.signasl.org/sign/"

# # Function to search and display ASL phrase video
# def search_asl_phrase(phrase):
#     # Replace spaces with hyphens for multi-word phrases
#     formatted_phrase = phrase.replace(" ", "-")
#     phrase_url = f"{asl_website}{formatted_phrase}"
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
#     phrase = input("Enter a phrase to search for (e.g., hello, how are you): ").strip().lower()
#     search_asl_phrase(phrase)

# if __name__ == "__main__":
#     main()
import requests
from bs4 import BeautifulSoup
import webbrowser

# Base URL of the ASL website
asl_website = "https://www.signasl.org/sign/"

# Function to search and extract ASL video URL
def search_asl_phrase(phrase):
    # Replace spaces with hyphens for multi-word phrases
    formatted_phrase = phrase.replace(" ", "-")
    phrase_url = f"{asl_website}{formatted_phrase}"
    print(f"Checking URL: {phrase_url}")
    
    try:
        # Fetch the page content of the phrase's URL
        response = requests.get(phrase_url)
        
        # Check if the page is found
        if response.status_code == 200:
            # Parse the page using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Try to find the video URL (you can inspect the webpage structure to adjust this)
            video_tag = soup.find('video')
            
            # If a video is found, extract the video URL and open it
            if video_tag and video_tag.find('source'):
                video_url = video_tag.find('source')['src']
                print(f"Found video for '{phrase}': {video_url}")
                webbrowser.open(video_url)  # Open the video in the browser
            else:
                print(f"No video found for: {phrase}")
        else:
            print(f"Page not found for phrase: {phrase_url}")
    
    except requests.RequestException as e:
        print(f"An error occurred while searching: {e}")

# Main function
def main():
    print("ASL Phrase Video Finder")
    phrase = input("Enter a phrase to search for (e.g., hello, how are you): ").strip().lower()
    search_asl_phrase(phrase)

if __name__ == "__main__":
    main()

