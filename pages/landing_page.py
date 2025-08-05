from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select

from pages.base_page import BasePage


class LandingPage(BasePage):
    # Locators
    select_departure = (By.ID, "select2-departCity-container")
    select_arrival = (By.ID, "select2-arrivalCity-container")
    from_search_input = (By.XPATH, "//input[contains(@class, 'select2-search__field')]")
    cookie_close_button = (By.ID, "tcCloseBtn")
    search_button = (By.CSS_SELECTOR, "button.btn.btn-primary.pull-right")

    def dismiss_popups(self):
        try:
            self.driver.find_element(By.ID, "tcCloseBtn").click()
            print("Cookie popup closed.")
        except:
            print("Cookie popup not found or already dismissed.")

        try:
            self.driver.find_element(By.TAG_NAME, "body").click()
            print("Power bank popup closed by clicking body.")
        except:
            print("Could not click body to close power bank popup.")

    def select_departure_city(self, city_name):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.select_departure)).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.from_search_input)).send_keys(city_name, Keys.ENTER)

    def select_arrival_city(self, city_name):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.from_search_input)).send_keys(city_name, Keys.ENTER)

    def select_date(self, day, month, year):
        xpath = f"//td[@data-handler='selectDay' and @data-month='{month}' and @data-year='{year}']/a[text()='{day}']"
        date_locator = (By.XPATH, xpath)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(date_locator)).click()

    def click_search_flights(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.search_button)).click()

    def select_first_flight_option(self):
        try:
            element = self.driver.find_element(By.XPATH, "(//li[contains(@class, 'eco') and contains(@class, 'select_out')])[1]")
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            self.driver.execute_script("arguments[0].click();", element)
            print("Clicked first available flight option.")
        except Exception as e:
            print(f"Failed to click departure flight: {e}")

    def scroll_to_return_flight_table(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "divIBFlightResultsOuter")))
            element = self.driver.find_element(By.ID, "divIBFlightResultsOuter")
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            print("Scrolled to return flight table (Surabaya → Jakarta).")
        except:
            print("Return flight table not found.")

    def select_return_flight_option(self):
        try:
            element = self.driver.find_element(By.XPATH, "(//li[contains(@class, 'eco') and contains(@class, 'select_in')])[1]")
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            self.driver.execute_script("arguments[0].click();", element)
            print("Clicked return flight option.")
        except Exception as e:
            print(f"Failed to click return flight option: {e}")

    def click_continue_button(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "btnContinue")))
            button = self.driver.find_element(By.ID, "btnContinue")
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "btnContinue")))
            button.click()
            print("Clicked the Continue button.")
        except Exception as e:
            print(f"Failed to click Continue button: {e}")

    def input_first_name(self, name):
        try:
            name_field = self.driver.find_element(By.ID, "ucPassenger1_lstPassenger_FIRSTNAME_0_txtFName_0")
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", name_field)
            name_field.clear()
            name_field.send_keys(name)
            print(f"Entered first name: {name}")
        except Exception as e:
            print(f"Failed to input first name: {e}")

    def input_last_name(self, last_name):
        try:
            last_name_field = self.driver.find_element(By.ID, "ucPassenger1_lstPassenger_LASTNAME_0_txtLName_0")
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", last_name_field)
            last_name_field.clear()
            last_name_field.send_keys(last_name)
            print(f"Entered last name: {last_name}")
        except Exception as e:
            print(f"Failed to input last name: {e}")

    def select_nationality_indonesia(self):
        try:
            dropdown = Select(self.driver.find_element(By.ID, "ucPassenger1_lstPassenger_NATIONALITY_0_ddlNationality_0"))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", dropdown._el)
            dropdown.select_by_value("IDN")
            print("Nationality set to Indonesia.")
        except Exception as e:
            print(f"Failed to select nationality: {e}")

    def input_phone_number(self, phone_number):
        try:
            phone_field = self.driver.find_element(By.ID, "ucPassenger1_lstPassenger_PAXMOBILENO_0_txtPaxMobileNo_0")
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", phone_field)
            phone_field.clear()
            phone_field.send_keys(phone_number)
            print(f"Entered phone number: {phone_number}")
        except Exception as e:
            print(f"Failed to input phone number: {e}")

    def click_passenger_continue_button(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "btnConfirmPassenger")))
            button = self.driver.find_element(By.ID, "btnConfirmPassenger")
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "btnConfirmPassenger")))
            button.click()
            print("Clicked final Continue button on passenger form.")
        except Exception as e:
            print(f"Failed to click final Continue button: {e}")

    def click_proceed_booking(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "btnProceedBooking"))
            ).click()
            print("Clicked 'Continue' (btnProceedBooking) successfully.")
        except Exception as e:
            print(f"Failed to click 'Continue' (btnProceedBooking): {e}")
