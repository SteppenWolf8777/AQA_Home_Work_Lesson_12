import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pathlib import Path


class RegistrationPage:
    URL = "https://demoqa.com/automation-practice-form"

    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    GENDER_MALE = (By.CSS_SELECTOR, "label[for='gender-radio-1']")
    GENDER_FEMALE = (By.CSS_SELECTOR, "label[for='gender-radio-2']")
    MOBILE = (By.ID, "userNumber")
    DATE_OF_BIRTH = (By.ID, "dateOfBirthInput")
    SUBJECTS = (By.ID, "subjectsInput")
    HOBBIES_SPORTS = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']")
    HOBBIES_READING = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-2']")
    HOBBIES_MUSIC = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-3']")
    CURRENT_ADDRESS = (By.ID, "currentAddress")
    STATE = (By.ID, "state")
    CITY = (By.ID, "city")
    SUBMIT_BUTTON = (By.ID, "submit")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Open url /automation-practice-form")
    def open(self):
        self.driver.get(self.URL)
        wrapper = self.driver.find_element(By.CSS_SELECTOR, ".practice-form-wrapper")
        assert "Student Registration Form" in wrapper.text
        # self.driver.execute_script("$('footer').remove()")
        # self.driver.execute_script("$('#fixedban').remove()")

    @allure.step("Fill first name field with {first_name}")
    def fill_first_name(self, first_name):
        """Fill first name field"""
        element = self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME))
        element.clear()
        element.send_keys(first_name)

    @allure.step("Fill last name field with {last_name}")
    def fill_last_name(self, last_name):
        """Fill last name field"""
        element = self.driver.find_element(*self.LAST_NAME)
        element.clear()
        element.send_keys(last_name)

    @allure.step("Fill email field with {email}")
    def fill_email(self, email):
        """Fill email field"""
        element = self.driver.find_element(*self.EMAIL)
        element.clear()
        element.send_keys(email)

    @allure.step("Fill gender")
    def fill_gender(self):
        """Fill gender field"""
        self.driver.find_element(*self.GENDER_MALE).click()

    @allure.step("Fill number field with {number}")
    def fill_number(self, number):
        """Fill number field"""
        element = self.driver.find_element(*self.MOBILE)
        element.clear()
        element.send_keys(number)

    @allure.step("Fill dateOfBirth")
    def fill_date_of_birth(self):
        """Fill dateOfBirth"""
        self.driver.find_element(*self.DATE_OF_BIRTH).click()
        self.driver.find_element(By.CSS_SELECTOR, ".react-datepicker__month-select").click()
        self.driver.find_element(By.CSS_SELECTOR, ".react-datepicker__month-select option[value='11']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".react-datepicker__year-select").click()
        self.driver.find_element(By.CSS_SELECTOR, ".react-datepicker__year-select option[value='1999']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[aria-label='Choose Sunday, December 5th, 1999']").click()

    @allure.step("Fill Subjects field with {subjects}")
    def fill_subjects(self, subjects):
        """Fill subjects field"""
        element = self.driver.find_element(*self.SUBJECTS)
        element.clear()
        element.send_keys(subjects)
        element.send_keys(Keys.ENTER)

    @allure.step("Fill Hobbies")
    def fill_hobbies(self):
        """Fill Hobbies field"""
        self.driver.find_element(*self.HOBBIES_SPORTS).click()

    @allure.step("Fill Photo")
    def fill_upload_photo(self, file_name: str = "test.jpg"):
        """Fill Photo field with specific file."""
        base_dir = Path(r"C:\Learning\AQA_Home_Work_Lesson_12\photo")
        file_path = base_dir / file_name
        wait = WebDriverWait(self.driver, 10)  # Используем self.driver из класса
        locator = (By.CSS_SELECTOR, "#uploadPicture")
        file_input = wait.until(EC.element_to_be_clickable(locator))
        file_input.send_keys(str(file_path.resolve()))

