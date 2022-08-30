import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class NewCustomerPageTest(unittest.TestCase):
    # initialization of webdriver
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        # get guru99 demo home page
        self.driver.get('https://demo.guru99.com/V1/index.php')
        self.login()

        time.sleep(3)
        self.driver.get("https://demo.guru99.com/V1/html/addcustomerpage.php")

    def tearDown(self):
        self.driver.quit()

    def login(self):
        driver = self.driver

        username_element = driver.find_element(By.NAME, "uid")
        username_element.send_keys('mngr432173')

        password_element = driver.find_element(By.NAME, "password")
        password_element.send_keys('narUqUm')

        driver.find_element(By.NAME, "btnLogin").click()

    # Verify Name Field
    def test_verify_name_field(self):
        driver = self.driver

        customer_name = driver.find_element(By.NAME, "name")  # get customer name input element
        customer_name_error = driver.find_element(By.XPATH, '//*[@id="message"]')  # get customer name error element

        # Name cannot be empty
        customer_name.send_keys()
        # press tab on the keyboard
        customer_name.send_keys(Keys.TAB)
        # assert for error messages
        self.assertEqual(customer_name_error.text, 'Customer name must not be blank')
        time.sleep(3)

        # Name cannot be numeric
        customer_name.send_keys('1234')
        # press tab on the keyboard
        customer_name.send_keys(Keys.TAB)
        # assert for error messages
        self.assertEqual(customer_name_error.text, 'Numbers are not allowed')
        time.sleep(3)

        # Name cannot have special characters
        customer_name.clear()
        customer_name.send_keys('name!@#')
        # press tab on the keyboard
        customer_name.send_keys(Keys.TAB)
        # assert for error messages
        self.assertEqual(customer_name_error.text, 'Special characters are not allowed')
        time.sleep(3)

        # Name cannot have first character as blank space
        customer_name.clear()
        customer_name.send_keys(' ')
        # press tab on the keyboard
        customer_name.send_keys(Keys.TAB)
        # assert for error messages
        self.assertEqual(customer_name_error.text, 'Numbers are not allowed')
        time.sleep(3)

    # select gender
    def click_gender(self):
        driver = self.driver

        # gender_male = driver.find_element(By.XPATH, "//*[.='male']")
        gender_female = driver.find_element(By.XPATH, "//*[.='female']")
        #
        # # click on a gender
        # gender_male.click()
        gender_female.click()
        # # press tab on the keyboard
        gender_female.send_keys(Keys.TAB)
        time.sleep(3)

    # # verify date field
    def test_verify_date_field(self):
        driver = self.driver
    #
        customer_date = driver.find_element(By.NAME, "dob")  # get customer date of birth input element
        # customer_date_error = driver.find_element(By.ID, "message24")  # get customer date of birth error element
    #
    #     # Date Field must not be blank
        customer_date.send_keys()
    #     # press tab on the keyboard
        customer_date.send_keys(Keys.TAB)
    #     # assert for error messages
    #     self.assertEqual(customer_date_error.text, 'Date Field must not be blank')
        time.sleep(3)


    # verify address field
    def test_verify_address_field(self):
        driver = self.driver
    #
        customer_address = driver.find_element(By.NAME, "addr")  # get customer address input element
        # customer_address_error = driver.find_element(By.ID, "message3")  # get customer address error element
    #
        # Address cannot be empty
        customer_address.send_keys()
        # press tab on the keyboard
        customer_address.send_keys(Keys.TAB)
        # assert for error messages
        # self.assertEqual(customer_address_error.text, '')
        time.sleep(3)

        # Address cannot have first blank space
        customer_address.clear()
        customer_address.send_keys(' ')
        # press tab on the keyboard
        customer_address.send_keys(Keys.TAB)
        # assert for error messages
        # self.assertEqual(customer_address_error.text, '')
        time.sleep(3)

        # verify city field
    def test_verify_city_field(self):
        driver = self.driver

        customer_city = driver.find_element(By.NAME, "city")  # get customer address input element
        customer_city_error = driver.find_element(By.ID, "message4")  # get customer address error element

        # City cannot be empty
        customer_city.send_keys()
        # press tab on the keyboard
        customer_city.send_keys(Keys.TAB)
        # assert for error messages
        self.assertEqual(customer_city_error.text, 'City Field must be nOT blank')
        time.sleep(3)

        # City cannot be numeric
        customer_city.send_keys('city123')
        # press tab on the keyboard
        customer_city.send_keys(Keys.TAB)
        # assert for error messages
        self.assertEqual(customer_city_error.text, 'Numbers are not allowed')
        time.sleep(3)

        # City cannot have special characters
        customer_city.clear()
        customer_city.send_keys('city!@#')
        # press tab on the keyboard
        customer_city.send_keys(Keys.TAB)
        # assert for error messages
        self.assertEqual(customer_city_error.text, 'Special characters are not allowed')
        time.sleep(3)

        # City cannot have first blank space
        customer_city.clear()
        customer_city.send_keys(' ')
        # press tab on the keyboard
        customer_city.send_keys(Keys.TAB)
        # assert for error messages
        self.assertEqual(customer_city_error.text, 'Numbers are not allowed')
        time.sleep(3)

        # verify state field
    def test_verify_state_field(self):
        driver = self.driver

        customer_state = driver.find_element(By.NAME, "state")  # get customer state input element
        customer_state_error = driver.find_element(By.ID, "message5")  # get customer state error element

        # State cannot be numeric
        customer_state.send_keys('State123')
        # press tab on the keyboard
        customer_state.send_keys(Keys.TAB)
        # assert for error messages
        self.assertEqual(customer_state_error.text, 'Numbers are not allowed')
        time.sleep(3)

        # City cannot have special character
        customer_state.clear()
        customer_state.send_keys('!@#')
        # press tab on the keyboard
        customer_state.send_keys(Keys.TAB)
        # assert for error messages
        self.assertEqual(customer_state_error.text, 'Special characters are not allowed')
        time.sleep(3)

        # State cannot have first blank space
        customer_state.clear()
        customer_state.send_keys(' ')
        # press tab on the keyboard
        customer_state.send_keys(Keys.TAB)
        # assert for error messages
        self.assertEqual(customer_state_error.text, 'Numbers are not allowed')
        time.sleep(3)

        # verify pin field
    def test_verify_pin_field(self):
        driver = self.driver

        customer_pin = driver.find_element(By.NAME, "pinno")  # get customer pin input element
        customer_pin_error = driver.find_element(By.ID, "message6")  # get customer pin error element

        # Pin must be numeric
        customer_pin.send_keys('1234PIN')
        # press tab on the keyboard
        customer_pin.send_keys(Keys.TAB)
        # assert for error messages
        self.assertEqual(customer_pin_error.text, 'Characters are not allowed')
        time.sleep(3)

        # Pin cannot be empty
        customer_pin.clear()
        customer_pin.send_keys()
        # press tab on the keyboard
        customer_pin.send_keys(Keys.TAB)
        # assert for error messages
        self.assertEqual(customer_pin_error.text, 'PIN Code must not be blank')
        time.sleep(3)

        # Pin must have 6 digits
        customer_pin.send_keys('123')
        # press tab on the keyboard
        customer_pin.send_keys(Keys.TAB)
        # assert for error messages
        self.assertEqual(customer_pin_error.text, 'PIN Code must have 6 Digits')
        time.sleep(3)

        # Pin cannot have special character
        customer_pin.clear()
        customer_pin.send_keys('123!@#')
        # press tab on the keyboard
        customer_pin.send_keys(Keys.TAB)
        # assert for error messages
        self.assertEqual(customer_pin_error.text, 'Special characters are not allowed')
        time.sleep(3)

        # Pin cannot have first blank space
        customer_pin.clear()
        customer_pin.send_keys(' ')
        # press tab on the keyboard
        customer_pin.send_keys(Keys.TAB)
        # assert for error messages
        self.assertEqual(customer_pin_error.text, 'Characters are not allowed')
        time.sleep(3)

        # Pin cannot have blank space
        customer_pin.clear()
        customer_pin.send_keys('123 45')
        # press tab on the keyboard
        customer_pin.send_keys(Keys.TAB)
        # assert for error messages
        self.assertEqual(customer_pin_error.text, 'Characters are not allowed')
        time.sleep(3)

        # verify Telephone field
    def test_verify_mobilenumber_field(self):
        driver = self.driver

        customer_mobilenumber = driver.find_element(By.NAME, "telephoneno")  # get customer mobilenumber input element
        customer_mobilenumber_error = driver.find_element(By.ID, "message7")  # get customer mobilenumber error element

        # Telephone cannot be empty
        customer_mobilenumber.send_keys()
        # press tab on the keyboard
        customer_mobilenumber.send_keys(Keys.TAB)
        # assert for error messages
        self.assertEqual(customer_mobilenumber_error.text, 'Telephone no must not be blank')
        time.sleep(3)

        # Telephone cannot have first character as blank space
        customer_mobilenumber.send_keys(' ')
        # press tab on the keyboard
        customer_mobilenumber.send_keys(Keys.TAB)
        # assert for error messages
        self.assertEqual(customer_mobilenumber_error.text, 'Characters are not allowed')
        time.sleep(3)

        # Telephone cannot have spaces
        customer_mobilenumber.clear()
        customer_mobilenumber.send_keys('123 123')
        # press tab on the keyboard
        customer_mobilenumber.send_keys(Keys.TAB)
        # assert for error messages
        self.assertEqual(customer_mobilenumber_error.text, 'Characters are not allowed')
        time.sleep(3)

        # Telephone cannot have special character
        customer_mobilenumber.clear()
        customer_mobilenumber.send_keys('88663682!@')
        # press tab on the keyboard
        customer_mobilenumber.send_keys(Keys.TAB)
        # assert for error messages
        self.assertEqual(customer_mobilenumber_error.text, 'Special characters are not allowed')
        time.sleep(3)

    def test_verify_email_field(self):
        driver = self.driver

        customer_email = driver.find_element(By.NAME, "emailid")  # get customer email input element
        customer_email_error = driver.find_element(By.ID, "message9")  # get customer email error element

        # email cannot be empty
        customer_email.send_keys()
        # press tab on the keyboard
        customer_email.send_keys(Keys.TAB)
        # assert for error messages
        self.assertEqual(customer_email_error.text, 'Email-ID must not be blank')
        time.sleep(3)

        # email must be in correct format
        customer_email.send_keys('guru99gmail.com')
        # press tab on the keyboard
        customer_email.send_keys(Keys.TAB)
        # assert for error messages
        self.assertEqual(customer_email_error.text, 'Email-ID is not valid')
        time.sleep(3)

        # email cannot have space
        customer_email.clear()
        customer_email.send_keys(' ')
        # press tab on the keyboard
        customer_email.send_keys(Keys.TAB)
        # assert for error messages
        self.assertEqual(customer_email_error.text, 'Email-ID is not valid')
        time.sleep(3)