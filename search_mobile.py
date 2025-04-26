import json
import time
import logging
import random
import requests
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# A function to wait for a few seconds, preventing too many requests
def wait_for(sec=2):
    time.sleep(sec)

# Mobile search

# Get number of words from command line argument, default to 20 if not provided
num_words = 20  # Default for mobile
if len(sys.argv) > 1:
    try:
        num_words = int(sys.argv[1])
        if num_words <= 0:
            print("Number of words must be positive. Using default (20).")
            num_words = 20
    except ValueError:
        print("Invalid number format. Using default (20).")

# Get random words from API
randomlists_url = f"https://random-word-api.herokuapp.com/word?number={num_words}"
response = requests.get(randomlists_url)
words_list = json.loads(response.text)
print('{0} words selected from {1}'.format(len(words_list), randomlists_url))

# Define mobile emulation with a randomly selected mobile user agent
mobile_user_agents = [
    "Mozilla/5.0 (Android 6.0.1; Mobile; rv:63.0) Gecko/63.0 Firefox/63.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36"
]

# Pick a random user agent
selected_user_agent = random.choice(mobile_user_agents)

# Configure mobile emulation settings
mobile_emulation = {
    "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
    "userAgent": selected_user_agent
}

# Set up Edge options with mobile emulation and anti-detection features
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("mobileEmulation", mobile_emulation)
edge_options.add_experimental_option("excludeSwitches", ["enable-automation"])
edge_options.add_experimental_option('useAutomationExtension', False)

# Create Edge WebDriver instance with options
driver = webdriver.Edge(options=edge_options)

# Set window size with slight randomization to appear more natural
window_width = random.randint(350, 390)
window_height = random.randint(620, 680)
driver.set_window_size(window_width, window_height)

# Add custom script to hide automation indicators
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    // Hide webdriver property
    Object.defineProperty(navigator, 'webdriver', {
        get: () => undefined
    });
    """
})

# Load Bing rewards page
driver.get("https://rewards.bing.com")
# Wait a randomized time on first page load
initial_wait = random.randint(8, 15)
wait_for(initial_wait)

# Perform mobile search actions
for num, word in enumerate(words_list):
    # Vary wait times between searches to mimic human behavior
    wait = random.randint(10, 30)
    print('{0}. Searching for: {1}, {2} secs'.format(str(num + 1), word, str(wait)))
    try:
        # Navigate to Bing
        driver.get("http://www.bing.com/")
        # Random wait before starting to type
        wait_for(random.uniform(1.5, 4.0))
        
        # Find search box
        search_box = driver.find_element(By.ID, "sb_form_q")
        search_box.clear()
        
        # Type search term with human-like timing
        for char in word:
            search_box.send_keys(char)
            # Mobile typing is usually a bit slower than desktop
            time.sleep(random.uniform(0.08, 0.35))
        
        # Occasionally "think" before pressing enter
        if random.random() < 0.3:  # 30% chance to pause longer
            time.sleep(random.uniform(1.0, 2.5))
        else:
            time.sleep(random.uniform(0.3, 1.0))
            
        search_box.send_keys(Keys.ENTER)
        
        # Occasionally scroll down on results page
        if random.random() < 0.4:  # 40% chance to scroll
            # Wait before scrolling
            time.sleep(random.uniform(2.0, 5.0))
            # Execute some scrolling
            scroll_amount = random.randint(300, 1000)
            driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
    except Exception as e1:
        logging.error('An error occurred: %s', e1)
    
    # Wait between searches with slight randomization
    wait_for(wait)

# Close the browser
driver.quit()
print("Done!")