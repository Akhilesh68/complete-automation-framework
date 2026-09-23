from selenium.webdriver.common.by import By


class HomePage:
    name_input = (By.XPATH, "//input[@name='name' and contains(@class,'form-control')]")
    email_input = (By.XPATH, "//input[@name='email']")
    password_input = (By.ID, "exampleInputPassword1")
    submit_btn = (By.XPATH, "//input[@type='submit']")
    alert = (By.XPATH, "//div[contains(@class , 'alert ')]")

    def __init__(self, driver):
        self.driver = driver

    def enter_name(self, name):
        return self.driver.find_element(*HomePage.name_input).send_keys(name)

    def enter_email(self, email):
        return self.driver.find_element(*HomePage.email_input).send_keys(email)

    def enter_password(self, password):
        return self.driver.find_element(*HomePage.password_input).send_keys(password)

    def click_submit_btn(self):
        return self.driver.find_element(*HomePage.submit_btn).click()

    def alert_msg(self):
        return self.driver.find_element(*HomePage.alert).text
