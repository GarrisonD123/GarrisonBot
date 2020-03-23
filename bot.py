
from selenium import webdriver
import os
from time import sleep


class GarrisonBot:

    def __init__(self, username, password):
        """""
        Initializes an instance of the GarrisonBot class.



        Args:
           username: str: The Instagram Username
           password: str: The Instagram Password

        Attributes:
                driver:Selenium.webdriver.Chrome: The Chromedriver that we use to automate browser actions
        """

        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com/'
        self.driver = webdriver.Chrome('chromedriver.exe')

        self.login()




    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        sleep(2)
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_element_by_xpath('//button[@type="submit"]') \
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]") \
            .click()
        sleep(2)

    def nav_user(self, user):
        self.driver.get('https://www.instagram.com/'+user)





if __name__ == '__main__':
    gr_bot = GarrisonBot('temp_user', 'temp_password')
    gr_bot.nav_user('garr.ison')

