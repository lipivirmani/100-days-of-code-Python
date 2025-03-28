import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"
FORM_URL = "https://forms.gle/FgFivPTusmYwV5z98"

# Selenium Browser Options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Initialize Selenium WebDriver
driver = webdriver.Chrome(options=chrome_options)

# 🏡 SCRAPING ZILLOW LISTINGS
def get_listings():
    """Scrapes Zillow for listings and extracts necessary details."""
    response = requests.get(ZILLOW_URL)
    soup = BeautifulSoup(response.text, "html.parser")
    listings = soup.find_all("li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")

    scraped_data = []

    for listing in listings:
        try:
            # Extract listing URL
            link = listing.find("a", class_="StyledPropertyCardDataArea-anchor")["href"]
            full_link = f"https://www.zillow.com{link}" if "http" not in link else link

            # Extract and clean the price
            price_text = listing.find("span", class_="PropertyCardWrapper__StyledPriceLine").text
            clean_price = re.sub(r"[^$\d,]", "", price_text).strip()

            # Extract and clean the address
            address_text = listing.find("address").text
            clean_address = re.sub(r"[\n|]+", "", address_text).strip()

            # Store the extracted data
            scraped_data.append({"address": clean_address, "price": clean_price, "link": full_link})

        except AttributeError:
            print("⚠️ Skipped a listing due to missing data.")
            continue

    return scraped_data


# ------------------------------ #
# 📝 FILLING GOOGLE FORM
# ------------------------------ #
def fill_form(listing_data):
    """Fills out the Google Form for each listing."""
    driver.get(FORM_URL)

    for listing in listing_data:
        try:
            # Wait for form fields to be visible
            wait = WebDriverWait(driver, 10)

            # Locate input fields
            address_field = wait.until(EC.presence_of_element_located(
                (By.XPATH, '//input[@type="text" and @aria-label]')))
            price_field = driver.find_elements(By.XPATH, '//input[@type="text" and @aria-label]')[1]
            link_field = driver.find_elements(By.XPATH, '//input[@type="text" and @aria-label]')[2]

            # Fill in the details
            address_field.send_keys(listing["address"])
            link_field.send_keys(listing["link"])
            price_field.send_keys(listing["price"])
            
            submit_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')))
            submit_button.click()

            # Wait for form submission to complete
            wait.until(EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "Submit another response")]')))

            print(f"✅ Submitted: {listing['address']}")

            # Reload form for the next submission
            driver.get(FORM_URL)

        except Exception as e:
            print(f"❌ Error filling form for {listing['address']}: {e}")

    print("\n🎉 All listings submitted successfully!")

# 🔥 EXECUTE THE SCRIPT

if __name__ == "__main__":
    # Scrape Zillow listings
    listings = get_listings()

    if listings:
        print(f"🔍 Found {len(listings)} listings. Starting form submission...")
        fill_form(listings)
    else:
        print("⚠️ No listings found. Exiting.")

    # Close the browser after execution
    driver.quit()
