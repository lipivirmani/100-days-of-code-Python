from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import os
import time


PROMISED_DOWN = 75
PROMISED_UP = 25

class InternetSpeedTwitterBot:
    def __init__(self, twitter_handle):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = 0
        self.up = 0
        self.twitter_handle = twitter_handle

    def get_internet_speed(self):
        """Fetches internet speed using Speedtest.net"""
        self.driver.get("https://www.speedtest.net/")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "start-text"))
        ).click()

        time.sleep(60)

        try:
            self.down = float(self.driver.find_element(By.CLASS_NAME, "download-speed").text)
            self.up = float(self.driver.find_element(By.CLASS_NAME, "upload-speed").text)
        except NoSuchElementException:
            print("Error: Could not fetch speed values.")
            self.down, self.up = None, None

    def login_to_twitter(self):
        """Logs in to Twitter"""
        self.driver.get("https://x.com/login")

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "text"))
        ).send_keys(os.getenv("TWITTER_USERNAME"), Keys.RETURN)

        try:
            password_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            password_field.send_keys(os.getenv("TWITTER_PASSWORD"), Keys.RETURN)
        except TimeoutException:
            print("Login Error: Check credentials or page layout changes.")
            return False

        time.sleep(5)  
        return True

    def tweet_at_provider(self):
        """Tweets only if internet speed is below the promised speed"""
        if self.down is None or self.up is None:
            print("Skipping tweet due to missing speed data.")
            return

        if self.down >= PROMISED_DOWN and self.up >= PROMISED_UP:
            print(f"Internet speed is fine: {self.down} Mbps / {self.up} Mbps. No need to tweet.")
            return  
        message = (f"@{self.twitter_handle} My internet speed is too slow! "
                   f"Download: {self.down} Mbps, Upload: {self.up} Mbps. "
                   f"Expected: {PROMISED_DOWN} Mbps / {PROMISED_UP} Mbps.")

        if self.login_to_twitter():
            tweet_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='tweetTextarea_0']"))
            )
            tweet_box.send_keys(message)
            tweet_box.send_keys(Keys.CONTROL, Keys.ENTER)
            print("Tweet sent successfully!")

        self.driver.quit()


bot = InternetSpeedTwitterBot("YourProviderHandle")
bot.get_internet_speed()
print(f"Download Speed: {bot.down} Mbps")
print(f"Upload Speed: {bot.up} Mbps")
bot.tweet_at_provider()
