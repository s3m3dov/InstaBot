# Imports
from selenium import webdriver
from time import sleep
from modules.utility_methods import xpaths, accounts
# Algorithm
class InstagramBot:
    def __init__(self, username, password):
        """
        Initializes an instance of the InstagramBot class. Call the login method to authenticate a user with IG
        Args:
            username:str: The Instagram username for a user
            password:str: The Instagram password for a user

        Attributes
            driver:Selenium.webdriver.Chrome: The Chromedriver that is used to automate browser actions
        """
        self.username = username
        self.password = password
        self.base_url = "https://www.instagram.com/"
    def login(self):
        self.driver = webdriver.Chrome('./chromedriver.exe')
        self.driver.get(f'{self.base_url}accounts/login/')
        sleep(2)
        try:
            self.driver.find_element_by_xpath(xpaths['accept_btn']).click()
            sleep(2)
        except:
            pass
        self.driver.find_element_by_xpath(xpaths['user_inp']).send_keys(self.username)
        self.driver.find_element_by_xpath(xpaths['pass_inp']).send_keys(self.password)
        self.driver.find_element_by_xpath(xpaths['login_btn']).click()
        sleep(2)
        try:
            self.driver.find_element_by_xpath(xpaths['notnow_btn']).click()
        except:
            pass
        sleep(1)
        try:
            self.driver.find_element_by_xpath(xpaths['notnow_btn']).click()
        except:
            pass
        print(f'{self.username} - logged in\n')
    def nav_user(self, user):
        """
        Navigates to the user page
        Args:
            user:str: The Instagram username for a user
        """
        self.driver.get(f'{self.base_url}{user}')
    def follow(self, user):
        """
        Follows a user
        Args:
            user:str: The Instagram username for a user
        """
        self.nav_user(user)
        sleep(1.5)
        try:
            self.driver.find_element_by_xpath(xpaths['flw_btn']).click()
            print(f'{user} - followed - {self.username}')
        except:
            print(f'{user} - following failed - {self.username}')
    def unfollow_user(self, user):
        """
        Unfollows a user
        Args:
            user:str: The Instagram username for a user
        """
        self.nav_user(user)
        sleep(2)
        try:
            self.driver.find_element_by_xpath(xpaths['unflw_btn_1a']).click()
            self.driver.find_element_by_xpath(xpaths['unflw_btn_2']).click()
            print(f'{user} - unfollowed - {self.username}')
        except:
            print(f'{user} - unfollowing failed - {self.username}')            
    def unfollow_org(self, user):
        self.nav_user(user)
        sleep(2)
        try:
            self.driver.find_element_by_xpath(xpaths['unflw_btn_1b']).click()
            self.driver.find_element_by_xpath(xpaths['unflw_btn_2']).click()
            print(f'{user} - unfollowed - {self.username}')
        except:
            print(f'{user} - unfollowing failed - {self.username}')
# Account objects
personal = InstagramBot(accounts['personal']['username'], accounts['personal']['password'])
professional1 = InstagramBot(accounts['professional1']['username'], accounts['professional1']['password'])
igbot_01 = InstagramBot(accounts['igbot_01']['username'], accounts['igbot_01']['password'])
igbot_02 = InstagramBot(accounts['igbot_02']['username'], accounts['igbot_02']['password'])
ortak1 = InstagramBot(accounts['ortak1']['username'], accounts['ortak1']['password'])
ortak2 = InstagramBot(accounts['ortak2']['username'], accounts['ortak2']['password'])
# Account objects list
acc_obj_all = [personal, professional1, igbot_01, igbot_02, ortak1, ortak2]
acc_obj_01 = [igbot_02, igbot_01]