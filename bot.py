
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

    def follow_user(self,user):
        self.nav_user(user)
        follow_button = self.driver.find_element_by_xpath("//button[contains(text(), 'Follow')]")
        follow_button.click()

    def unfollow_user(self, user):
        self.nav_user(user)
        follow_button = self.driver.find_element_by_xpath("//button[contains(text(), 'Following')]")
        follow_button.click()
        are_you_sure_button = self.driver.find_element_by_xpath("//button[contains(text(), 'Unfollow')]")
        are_you_sure_button.click()

    def get_num_pics(self,user):
        self.nav_user(user)
        pic_num_element = self.driver.find_element_by_class_name("g47SY ")
        pic_num = int(pic_num_element.text)
        return pic_num

    def select_picture(self,user, num = 0):
        self.nav_user(user)
        sleep(2)
        pictures_list = self.driver.find_elements_by_class_name('_9AhH0')
        #if num < self.get_num_pics('garr.ison'): TODO fix this if statement
        picture = pictures_list[num]
        picture.click()


    def like_picture(self,user,num = 0):
        self.nav_user(user)
        self.select_picture(user,num)
        sleep(2)
        like_button = self.driver.find_element_by_css_selector("[aria-label = Like]")
        like_button.click()



if __name__ == '__main__':
    gr_bot = GarrisonBot('garrison.bot', 'Dooley13')
    gr_bot.follow_user('saraafitzz')
    gr_bot.like_picture('garr.ison',1)





