from selenium import webdriver
from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

game_end = time.time() + 60*5
timeout = time.time() + 5

while True:
    try:
        the_cookie = driver.find_element(By.ID, value="cookie")
        buildings = {
            "time_machine": ("buyTime machine", 10),
            "portal": ("buyPortal", 10),
            "alchemy_lab": ("buyAlchemy lab", 25),
            "shipment": ("buyShipment", 20),
            "mine": ("buyMine", 7),
            "factory": ("buyFactory", 10),
            "grandma": ("buyGrandma", 17),
            "cursor": ("buyCursor", 21),
        }

        the_cookie.click()
        if time.time() > timeout:
            for name, (building_id, limit) in buildings.items():
                building = driver.find_element(By.ID, building_id)
                try:
                    amount_element = building.find_element(By.CLASS_NAME, "amount")
                    amount = int(amount_element.text)
                    if amount < limit:
                        building.click()
                        timeout = time.time() + 5

                except NoSuchElementException:
                    building.click()
                    timeout = time.time() + 5

    except StaleElementReferenceException:
        pass

    if time.time() > game_end:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break
