from getpass import getpass
from random import randint
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException, \
    NoSuchElementException, StaleElementReferenceException
import sys
from time import sleep

# If you don"t want to manually enter your netid and password
# every time, you can pass them as variables in your script

# args = sys.argv[1:]
# assert len(args) == 2
# netid, password = tuple(args)

# Get users netid and password
netid = input("  netid > ")
password = getpass()

# Headless Chrome
options = webdriver.ChromeOptions()
options.add_argument("--disable-extensions")
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--incognito")
options.add_argument("--window-size=1920,2880")
driver = webdriver.Chrome(options=options)

url = "https://dailycheck.cornell.edu/saml_login_user?redirect=%2Fdaily-checkin"
driver.get(url)

try:
    # Login
    driver.find_element_by_id("netid").send_keys(netid)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_class_name("input-submit").click()

    # Ensure daily check not already complete
    # Exit otherwise
    try:
        driver.find_element_by_id("continue").click()
    except (ElementNotInteractableException, NoSuchElementException):
        text = driver.find_element_by_css_selector("div.message__single.mask_img") \
                     .find_elements_by_tag_name("p")[1].text
        if "Thank you for completing your Daily Check." in text:
            print("Daily Check Already Complete")
        else:
            print("Unexpected Error")
        exit()

    # Check "no" for all questions
    driver.find_element_by_id("covidsymptoms-no").click()
    driver.find_element_by_id("contactsymptoms-no").click()
    driver.find_element_by_id("exposure-no").click()
    driver.find_element_by_id("positivetestever-no").click()

    # Submit x2
    sleep(randint(3, 6))  # pausing in case they
    driver.find_element_by_id("submit").click()

    sleep(randint(3, 6))
    driver.find_element_by_id("submit").click()

    driver.close()
    print(f"Successfully completed {netid}\'s daily check")

except (ElementClickInterceptedException, ElementNotInteractableException, NoSuchElementException,
        StaleElementReferenceException):
    print("Unexpected Failure")
