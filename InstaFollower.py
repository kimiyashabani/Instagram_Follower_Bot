from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time
class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
    def login(self,user_name,user_password):
        self.driver.get("https://www.instagram.com/accounts/login/")
        # Check if the cookie warning is present on the page
        time.sleep(2.5)
        button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(),'Allow all cookies')]")
        button.click()
        username = self.driver.find_element(By.NAME, value='username')
        password = self.driver.find_element(By.NAME, value='password')
        username.send_keys(user_name, Keys.ENTER)
        password.send_keys(user_password, Keys.ENTER)

        # Click "Not now" and ignore Save-login info prompt
        time.sleep(4.3)
        save_login_prompt = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
        if save_login_prompt:
            save_login_prompt.click()

        # Click "Not now" and ignore the Turn on notification
        time.sleep(3.7)
        notifications_prompt = self.driver.find_element(by=By.XPATH, value="// button[contains(text(), 'Not Now')]")
        if notifications_prompt:
            notifications_prompt.click()
    def find_followers(self,acc):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{acc}/followers/")
        time.sleep(5)
        modal_xpath ="/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div"
        modal = self.driver.find_element(By.XPATH, modal_xpath)
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)
    def follow(self):
        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, value =' _acan _acap _acas _aj1- _ap30')
        for button in follow_buttons:
            #following for the first time
            try:
                button.click()
                time.sleep(1.1)
            #when we have already followed someone:
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()

