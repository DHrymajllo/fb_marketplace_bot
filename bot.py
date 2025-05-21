import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from db import init_db, has_sent, log_sent
from config import *

def setup_driver():
    options = Options()
    # CHANGE PATH TO chromedriver.exe ↓
    service = Service("C:/Users/RyderX/Desktop/selenium_driver/chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def login_facebook(driver):
    driver.get("https://www.facebook.com")
    print("Please log in manually...")
    input("Press Enter after logging in...")

def search_marketplace(driver):
    driver.get(FB_URL)
    time.sleep(5)
    search_box = driver.find_element(By.XPATH, '//input[@placeholder="Search Marketplace"]')
    search_box.send_keys(KEYWORD)
    search_box.send_keys(KEYWORD)
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)

def collect_listings(driver):
    elements = driver.find_elements(By.XPATH, '//a[contains(@href, "/marketplace/item/")]')
    unique_links = list({el.get_attribute('href') for el in elements})
    return unique_links

def send_message(driver, url):
    driver.get(url)
    time.sleep(5)
    try:
        message_btn = driver.find_element(By.XPATH, '//div[@aria-label="Message"]')
        message_btn.click()
        time.sleep(2)
        textbox = driver.find_element(By.XPATH, '//div[@aria-label="Message"]//div[@contenteditable="true"]')
        textbox.send_keys(MESSAGE_TEXT)
        textbox.send_keys("\n")
        time.sleep(2)
        return True
    except Exception as e:
        print(f"Error on {url}: {e}")
        return False

def main():
    init_db()
    driver = setup_driver()
    login_facebook(driver)
    search_marketplace(driver)
    listings = collect_listings(driver)

    messages_sent = 0
    for url in listings:
        listing_id = url.split('/')[-1].split('?')[0]
        if has_sent(listing_id):
            continue
        if send_message(driver, url):
            log_sent(listing_id)
            messages_sent += 1
            print(f"Sent message to: {url}")
        if messages_sent >= MAX_MESSAGES_PER_DAY:
            break
        time.sleep(5)

    driver.quit()

if __name__ == "__main__":
    main()
