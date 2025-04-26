import json
import random
import time
import requests
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# A function to wait for a few seconds, preventing too many requests
def wait_for(sec=2):
    time.sleep(sec)

# PC search

# Get number of words from command line argument, default to 30 if not provided
num_words = 30  # Default value
if len(sys.argv) > 1:
    try:
        num_words = int(sys.argv[1])
        if num_words <= 0:
            print("Number of words must be positive. Using default (30).")
            num_words = 30
    except ValueError:
        print("Invalid number format. Using default (30).")

# Get a list of words from randomlists.com
randomlists_url = f"https://random-word-api.herokuapp.com/word?number={num_words}"
response = requests.get(randomlists_url)
words_list = json.loads(response.text)
print('{0} words selected from {1}'.format(len(words_list), randomlists_url))

# Setup Edge options with stealth settings
options = webdriver.EdgeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# Initialize Edge driver with options
driver = webdriver.Edge(options=options)

# Add custom scripts to mask automation indicators
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    // Overwrite the 'navigator.webdriver' property to undefined
    Object.defineProperty(navigator, 'webdriver', {
        get: () => undefined
    });
    """
})

wait_for()
driver.get("https://rewards.bing.com")
wait_for(30)

# Perform pc search actions
for num, word in enumerate(words_list):
    # Add more randomness to wait times to appear more human-like
    wait = random.randint(10, 30)
    print('{0}. Searching for: {1}, {2} secs'.format(str(num + 1), word, str(wait)))
    try:
        driver.get("http://www.bing.com/")
        # Random wait before starting to type
        wait_for(random.uniform(1.5, 4.0))

        # Find search box
        search_box = driver.find_element(By.ID, "sb_form_q")
        search_box.clear()
        
        # Type like a human with random delays between keystrokes
        for char in word:
            search_box.send_keys(char)
            time.sleep(random.uniform(0.05, 0.25))
        
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