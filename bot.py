
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
        self.pic_num = 0

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

    def get_num_pics(self,user = 'garrison.bot'):
        self.nav_user(user)
        pic_num_element = self.driver.find_element_by_class_name("g47SY")
        self.pic_num = int(pic_num_element.text)


    def select_picture(self,user, num = 0):
        self.nav_user(user)
        self.get_num_pics(user)
        sleep(2)
        pictures_list = self.driver.find_elements_by_class_name('_9AhH0')
        #if num < self.get_num_pics('garr.ison'): TODO fix this if statement
        print(self.pic_num)
        picture = pictures_list[num]
        picture.click()


    def like_picture(self,user,num = 0):
        self.nav_user(user)
        self.select_picture(user,num)
        sleep(2)
        like_button = self.driver.find_element_by_css_selector("[aria-label = Like]")
        like_button.click()

    def like_all_pictures(self,user):
        self.nav_user(user)
        self.select_picture(user)
        sleep(2)
        for x in range(0,self.pic_num-1):
            sleep(10)
            like_button = self.driver.find_element_by_css_selector("[aria-label = Like]")
            like_button.click()
            next_button = self.driver.find_element_by_link_text("Next")
            next_button.click()
        sleep(2)
        like_button = self.driver.find_element_by_css_selector("[aria-label = Like]")
        like_button.click()

    def follow_for_follow(self):
        self.nav_user(self.username)
        sleep(2)
        followers_button = self.driver.find_element_by_xpath("//a[contains(@href, '/"+self.username+"/followers/')]")
        followers_button.click()
        sleep(2)
        not_following_list = self.driver.find_elements_by_xpath("//button[contains(text(), 'Follow')]")
        for x in range(0,self.pic_num):
            if not_following_list[x].text == 'Follow':
                not_following_list[x].click()






if __name__ == '__main__':
    gr_bot = GarrisonBot('garrison.bot', 'PASSWORD')
    gr_bot.get_num_pics("garr.ison")
    gr_bot.follow_for_follow()





