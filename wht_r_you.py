#!/usr/bin/env python3

import requests
import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

def get_website_content(url):
    # Add http:// if not present in the URL
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    
    try:
        # Send GET request to the website
        response = requests.get(url)
        # Raise an exception for bad status codes
        response.raise_for_status()
        # Print the HTML content
        print("HTML Response:")
        print(response.text)
        
        # Take screenshot
        take_screenshot(url)
        
    except requests.RequestException as e:
        print(f"Error occurred during GET request: {e}")
        sys.exit(1)

def take_screenshot(url):
    try:
        print("\nTaking screenshot...")
        
        # Configure Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")  # Updated headless mode
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")
        
        # Initialize Chrome driver with updated service creation
        service = Service()
        driver = webdriver.Chrome(
            options=chrome_options,
            service=service
        )
        
        # Navigate to the URL
        driver.get(url)
        
        # Create screenshots directory if it doesn't exist
        if not os.path.exists('screenshots'):
            os.makedirs('screenshots')
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshots/screenshot_{timestamp}.png"
        
        # Take screenshot
        driver.save_screenshot(filename)
        print(f"Screenshot saved as: {filename}")
        
        # Close the browser
        driver.quit()
        
    except Exception as e:
        print(f"Error occurred while taking screenshot: {e}")
        if 'driver' in locals():
            driver.quit()
        sys.exit(1)

def main():
    # Check if URL is provided as command line argument
    if len(sys.argv) != 2:
        print("Usage: python swiss_knf.py example.com")
        sys.exit(1)
    
    website = sys.argv[1]
    get_website_content(website)

if __name__ == "__main__":
    main()
