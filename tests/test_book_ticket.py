import os
import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.landing_page import LandingPage

def test_book_ticket():
    # Chrome options
    options = Options()
    options.add_argument("--log-level=3")  # Suppress warnings
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument("--start-maximized")  # Make browser wide

    # Setup WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.batikair.com")
    print("Browser launched and navigated to https://www.batikair.com")

    try:
        landing_page = LandingPage(driver)

        landing_page.dismiss_popups()
        print("Dismissed popups.")

        landing_page.select_departure_city("Jakarta")
        print("Typed Jakarta.")

        landing_page.select_arrival_city("Surabaya")
        print("Typed Surabaya.")

        landing_page.select_date(day='28', month='7', year='2025')
        print("Selected Departure Date.")

        landing_page.select_date(day='30', month='7', year='2025')
        print("Selected Return Date.")

        time.sleep(2)
        landing_page.click_search_flights()
        print("Clicked Search Flights button.")

        time.sleep(10)
        landing_page.select_first_flight_option()
        print("Select Departure Economy.")

        landing_page.scroll_to_return_flight_table()
        print("Scroll to Return Flights.")

        landing_page.select_return_flight_option()
        print("Select Return Economy.")

        time.sleep(2)
        landing_page.click_continue_button()
        print("Click Continue.")

        landing_page.input_first_name("Tengku")
        landing_page.input_last_name("Taufik")
        print("Input First and Last Name.")

        landing_page.select_nationality_indonesia()
        print("Select Indonesia Nationality.")

        landing_page.input_phone_number("81234567890")
        print("Input Phone Number.")

        time.sleep(5)
        landing_page.click_passenger_continue_button()
        print("Click Continue.")

        time.sleep(2)
        landing_page.click_proceed_booking()
        print("Click Continue to Payment,")
        time.sleep(5)

    except Exception as e:
        # Save screenshot on failure
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, f"error_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
        driver.save_screenshot(screenshot_path)
        print(f"Test failed. Screenshot saved to {screenshot_path}")
        raise

    finally:
        time.sleep(10)
        driver.quit()
        print("Browser closed.")
