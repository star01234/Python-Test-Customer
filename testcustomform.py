from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class TestTco1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="D:\\webdriver\\chromedriver.exe")

    def test(self):
        self.driver.get("http://localhost/customer/index.html")
        time.sleep(1)
        firstNameInput = self.driver.find_element(By.ID, "firstName")
        firstNameInput.send_keys("johnjohn")
        lastNameInput = self.driver.find_element(By.ID, "lastName")
        lastNameInput.send_keys("canonc")
        ageInput = self.driver.find_element(By.ID, "age")
        ageInput.send_keys("2")
        submitButton = self.driver.find_element(By.TAG_NAME, "button")
        submitButton.click()
        
        result = self.driver.find_element(By.ID, "firstname").text
        self.assertEqual("First Name: johnjohn", result)

        self.driver.save_screenshot("img/test_case1.png")

    def tearDown(self):
        self.driver.quit()

    def test_2(self):
        self.driver.get("http://localhost/customer/index.html")

        firstNameInput = self.driver.find_element(By.ID, "firstName")
        firstNameInput.send_keys("johnj")
        lastNameInput = self.driver.find_element(By.ID, "lastName")
        lastNameInput.send_keys("canoncanoncano")
        ageInput = self.driver.find_element(By.ID, "age")
        ageInput.send_keys("149")
        submitButton = self.driver.find_element(By.TAG_NAME, "button")
        submitButton.click()

        result = self.driver.find_element(By.ID, "firstname").text
        self.assertEqual("First Name: johnj", result)

        self.driver.save_screenshot("img/test_case2.png")

    def tearDown(self):
        self.driver.quit()

    def test_3(self):
        self.driver.get("http://localhost/customer/index.html")

        firstNameInput = self.driver.find_element(By.ID, "firstName")
        firstNameInput.send_keys("johnjo")
        lastNameInput = self.driver.find_element(By.ID, "lastName")
        lastNameInput.send_keys("canoncanoncanon")
        ageInput = self.driver.find_element(By.ID, "age")
        ageInput.send_keys("150")
        submitButton = self.driver.find_element(By.TAG_NAME, "button")
        submitButton.click()
        
        result = self.driver.find_element(By.ID, "firstname").text
        self.assertEqual("First Name: johnjo", result)

        self.driver.save_screenshot("img/test_case3.png")

    def tearDown(self):
        self.driver.quit()

    def test_4(self):
        self.driver.get("http://localhost/customer/index.html")

        firstNameInput = self.driver.find_element(By.ID, "firstName")
        firstNameInput.send_keys("johnjohnjohnjo")
        lastNameInput = self.driver.find_element(By.ID, "lastName")
        lastNameInput.send_keys("canoncan")
        ageInput = self.driver.find_element(By.ID, "age")
        ageInput.send_keys("75")
        submitButton = self.driver.find_element(By.TAG_NAME, "button")
        submitButton.click()
        
        result = self.driver.find_element(By.ID, "firstname").text
        self.assertEqual("First Name: johnjohnjohnjo", result)
        self.driver.save_screenshot("img/test_case4.png")

    def tearDown(self):
        self.driver.quit()

    def test_5(self):
        self.driver.get("http://localhost/customer/index.html")

        firstNameInput = self.driver.find_element(By.ID, "firstName")
        firstNameInput.send_keys("johnjohnjohnjoh")
        lastNameInput = self.driver.find_element(By.ID, "lastName")
        lastNameInput.send_keys("canoncan")
        ageInput = self.driver.find_element(By.ID, "age")
        ageInput.send_keys("75")
        submitButton = self.driver.find_element(By.TAG_NAME, "button")
        submitButton.click()
        
        result = self.driver.find_element(By.ID, "firstname").text
        self.assertEqual("First Name: johnjohnjohnjoh", result)

        self.driver.save_screenshot("img/test_case5.png")

    def tearDown(self):
        self.driver.quit()

    def test_6(self):
        self.driver.get("http://localhost/customer/index.html")

        firstNameInput = self.driver.find_element(By.ID, "firstName")
        firstNameInput.send_keys("john")
        lastNameInput = self.driver.find_element(By.ID, "lastName")
        lastNameInput.send_keys("canoncan")
        ageInput = self.driver.find_element(By.ID, "age")
        ageInput.send_keys("75")
        submitButton = self.driver.find_element(By.TAG_NAME, "button")
        submitButton.click()
        
        result = self.driver.find_element(By.ID, "name").text
        self.assertEqual("Modern Form", result)

        self.driver.save_screenshot("img/test_case6.png")

    def tearDown(self):
        self.driver.quit()

    def test_8(self):
        self.driver.get("http://localhost/customer/index.html")

        firstNameInput = self.driver.find_element(By.ID, "firstName")
        firstNameInput.send_keys("johnjohn")
        lastNameInput = self.driver.find_element(By.ID, "lastName")
        lastNameInput.send_keys("cano")
        ageInput = self.driver.find_element(By.ID, "age")
        ageInput.send_keys("149")
        submitButton = self.driver.find_element(By.TAG_NAME, "button")
        submitButton.click()
        
        result = self.driver.find_element(By.ID, "name").text
        self.assertEqual("Modern Form", result)

        self.driver.save_screenshot("img/test_case8.png")

    def tearDown(self):
        self.driver.quit()

    def test_10(self):
        self.driver.get("http://localhost/customer/index.html")

        firstNameInput = self.driver.find_element(By.ID, "firstName")
        firstNameInput.send_keys("johnjohn")
        lastNameInput = self.driver.find_element(By.ID, "lastName")
        lastNameInput.send_keys("canoncan")
        ageInput = self.driver.find_element(By.ID, "age")
        ageInput.send_keys("0")
        submitButton = self.driver.find_element(By.TAG_NAME, "button")
        submitButton.click()
        
        result = self.driver.find_element(By.ID, "name").text
        self.assertEqual("Modern Form", result)

        self.driver.save_screenshot("img/test_case10.png")

    def tearDown(self):
        self.driver.quit()

    def test_11(self):
        self.driver.get("http://localhost/customer/index.html")

        firstNameInput = self.driver.find_element(By.ID, "firstName")
        firstNameInput.send_keys("johnjohn")
        lastNameInput = self.driver.find_element(By.ID, "lastName")
        lastNameInput.send_keys("canonc")
        ageInput = self.driver.find_element(By.ID, "age")
        ageInput.send_keys("151")
        submitButton = self.driver.find_element(By.TAG_NAME, "button")
        submitButton.click()
        
        result = self.driver.find_element(By.ID, "name").text
        self.assertEqual("Modern Form", result)

        self.driver.save_screenshot("img/test_case11.png")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
