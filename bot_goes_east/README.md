# Satellite Image Bot

@terra_fotos_bot

This Python script automates the process of fetching satellite images from specific websites and posting them on Twitter. It utilizes Selenium for web automation and Tweepy for interacting with the Twitter API.

## How it works

1. **Web Scraping**: The script uses Selenium to navigate to a specified website containing satellite images.
2. **Image Download**: It identifies and downloads the desired satellite image from the webpage.
3. **Twitter Posting**: After downloading the image, it posts the image along with a title on Twitter using the Tweepy library.

## Setup Instructions

1. **Install Dependencies**: Ensure you have Python installed on your system along with the necessary packages. You can install them using pip:

   ```
   pip install selenium webdriver-manager requests tweepy
   ```

2. **WebDriver Setup**: Download the appropriate WebDriver for your browser (in this case, Chrome) and ensure it is in your system's PATH or specify its path in the script.

3. **Twitter API Keys**: Obtain API keys and access tokens from Twitter Developer Portal and replace the placeholders in the script with your own keys.

4. **Run the Script**: Execute the Python script, and it will automatically fetch the satellite image and post it on Twitter.

## Note

- The script is designed to work with specific websites and may require adjustments if the website layout or structure changes.
- Ensure compliance with the terms of service of the websites scraped and the Twitter API usage policy to avoid any violations.

For any issues or queries, feel free to contact the script author.