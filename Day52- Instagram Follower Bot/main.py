from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

# Change this to an account of your choice
SIMILAR_ACCOUNT = "businessbrite"
USERNAME = "YOUR_USERNAME"
PASSWORD = "YOUR_PASSWORD"


class InstaFollower:
    def __init__(self):
        """Initialize Chrome driver with options."""
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        """Logs into Instagram."""
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(random.uniform(4, 6))

        try:
            # Dismiss cookie warning if present
            cookie_warning = self.driver.find_elements(By.XPATH, "//button[contains(text(), 'Only allow essential cookies')]")
            if cookie_warning:
                cookie_warning[0].click()
                time.sleep(2)

            username_input = self.driver.find_element(By.NAME, "username")
            password_input = self.driver.find_element(By.NAME, "password")

            username_input.send_keys(USERNAME)
            password_input.send_keys(PASSWORD)
            time.sleep(random.uniform(1.5, 3))
            password_input.send_keys(Keys.ENTER)

            time.sleep(random.uniform(5, 7))

            # Handle "Save Login Info" pop-up
            try:
                save_login_prompt = self.driver.find_element(By.XPATH, "//div[contains(text(), 'Not now')]")
                save_login_prompt.click()
                time.sleep(random.uniform(2, 4))
            except NoSuchElementException:
                pass

            # Handle "Turn on Notifications" pop-up
            try:
                notifications_prompt = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]")
                notifications_prompt.click()
                time.sleep(random.uniform(2, 4))
            except NoSuchElementException:
                pass

        except NoSuchElementException:
            print("Error logging in. Check username/password or Instagram UI changes.")

    def find_followers(self):
        """Opens the followers list of the target account and scrolls down."""
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers/")
        time.sleep(random.uniform(7, 10))

        try:
            # Locate the followers modal
            modal_xpath = "//div[@role='dialog']//div[@class='_aano']"
            modal = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, modal_xpath))
            )

            for _ in range(random.randint(5, 7)):  # Scroll 5-7 times
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
                time.sleep(random.uniform(2, 3))

        except NoSuchElementException:
            print("Error finding followers. UI might have changed.")

    def follow(self):
        """Finds and clicks 'Follow' buttons."""
        try:
            all_buttons = self.driver.find_elements(By.XPATH, "//button[contains(text(), 'Follow')]")

            for button in all_buttons:
                try:
                    button.click()
                    time.sleep(random.uniform(1, 3))
                except ElementClickInterceptedException:
                    try:
                        cancel_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Cancel')]")
                        cancel_button.click()
                    except NoSuchElementException:
                        print("Cancel button not found.")

        except NoSuchElementException:
            print("No follow buttons found.")

        print("Finished following!")

    def close_browser(self):
        self.driver.quit()


# Run the bot
bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
bot.close_browser()
