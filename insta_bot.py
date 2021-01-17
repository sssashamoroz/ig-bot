import credentials as credentials

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from random import randint

class instagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(3)

        #insert username
        user_name_field = driver.find_element_by_xpath("//input[@name='username']")
        user_name_field.clear()
        user_name_field.send_keys(self.username)
        time.sleep(1)

        #insert pass
        user_pass_field = driver.find_element_by_xpath("//input[@name='password']")
        user_pass_field.clear()
        user_pass_field.send_keys(self.password)
        user_pass_field.send_keys(Keys.RETURN)
        time.sleep(5)

        #dodge
        not_now_one = driver.find_element_by_xpath("//html/body/div[1]/section/main/div/div/div/div/button")
        not_now_one.click()
        time.sleep(3)
        not_now_two = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
        not_now_two.click()
        time.sleep(2)


    def commentPics(self):
        driver = self.driver
        posts = []

        while True:
            for i in range(1,5):
                like = driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[1]/div[2]/div/article[" + str(i) + "]/div[3]/section[1]/span[1]/button/div")
                like.click()
                time.sleep(1)
                
            time.sleep(3)
            driver.execute_script("window.scrollBy(0, 20000);")
            driver.execute_script("window.scrollBy(0, 20000);")
            time.sleep(3)
                                            

bot = instagramBot(credentials.username, credentials.password)
bot.login()
time.sleep(3)
bot.commentPics()

