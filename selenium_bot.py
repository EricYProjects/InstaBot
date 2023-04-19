from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class InstaBot():
    def __init__(self, username_input, password_input):
        #Object attributes
        self.driver = webdriver.Chrome()
        self.username = username_input
        self.password = password_input
        self.following = []
        self.followers = []

        #Call object methods to run bot
        self.login(self.username, self.password)
        self.go_to_profile()
        self.find_following()
        self.find_followers()

    # 1 - Go to Instagram (sleeps to let page load)
    # 2 - Finds username & password input boxes
    # 3 - Enters credentials into input boxes (sleeps to let Login box become clickable)
    # 4 - Click login button
    def login(self, uname, pword):
        self.driver.get("https://instagram.com")
        time.sleep(4)
        insta_username_box = self.driver.find_element(By.NAME, 'username')
        insta_password_box = self.driver.find_element(By.NAME, 'password')
        insta_username_box.send_keys(uname)
        insta_password_box.send_keys(pword)
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, 'button._acan._acap._acas._aj1-').click()

    # 1 - Sleeps (for web page loading)
    # 2 - Goes to user's profile page
    def go_to_profile(self):
        time.sleep(5)
        self.driver.get(f"https://instagram.com/{self.username}")

    # 1 - Sleeps (for web page loading)
    # 2 - Finds list element (passed into function via topBarName) on Instagram web page that contains Posts [0], Followers [1], Following [2]
    # 3 - Clicks the element based on elementNum (which corresponds to the list values above)
    def openPopUp(self, topBarName, elementNum):
        time.sleep(5)
        top_bar_list = self.driver.find_elements(By.CLASS_NAME, topBarName)
        top_bar_list[elementNum].click()
        time.sleep(3)

    # 1 - Finds the pop up element that contains scrollbox of followers/following
    # 2 - Checks the pop up box for visible user profile picture elements in scroll box; if less than follower/following number, keep looping
    # 3 - Scrolls (with 1.2 delay to prevent bot-like spamming)
    def scroll(self, elementNum):
        popup = self.driver.find_element(By.CLASS_NAME, '_aano')

        last_height = self.driver.execute_script("return arguments[0].scrollHeight", popup)
        while True:
            self.driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", popup)
            time.sleep(1.5)
            new_height = self.driver.execute_script("return arguments[0].scrollHeight", popup)
            if new_height == last_height:
                self.driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", popup)
                time.sleep(3)
                break
            last_height = new_height
            print("Scrolling...")

    # 1 - Finds the pop up element that contains scrollbox of followers/following
    # 2 - initial_list gets all the elements in the scrollbox that contain usernames
    # 3 - Iterate through list of elements and save to the object's follower or following list
    #def usernames_to_selfList(self, saveOption):
    def usernames_to_selfList(self, saveOption):
        text = saveOption
        popup = self.driver.find_element(By.CLASS_NAME, '_aano')
        initial_list = popup.find_elements(By.CLASS_NAME, 'x1nhvcw1')

        attribute = getattr(self, saveOption, None)
        if attribute is not None:
            for num in range(len(initial_list)):
                attribute.append(initial_list[num].text)
                print(f"Adding Item {initial_list[num].text}")


    # 1 - Opens pop up scroll box
    # 2 - Scrolls
    # 3 - Finds usernames and adds to object's corresponding list
    # 4 - Go to original profile page
    def find_following(self):
        self.openPopUp(topBarName='xl565be', elementNum=2)
        self.scroll(elementNum=2)
        self.usernames_to_selfList(saveOption='following')
        self.go_to_profile()

    # 1 - Opens pop up scroll box
    # 2 - Scrolls
    # 3 - Finds usernames and adds to object's corresponding list
    # 4 - Go to original profile page
    def find_followers(self):
        self.openPopUp(topBarName='xl565be', elementNum=1)
        self.scroll(elementNum=1)
        self.usernames_to_selfList(saveOption='followers')
        self.go_to_profile()



