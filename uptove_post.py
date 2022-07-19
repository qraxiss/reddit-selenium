from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import pandas as pd

def login(driver, username, password):
    username_item = driver.find_element(by=By.ID, value='loginUsername')
    print(username_item.text)
    username_item.send_keys(username);sleep(1)

    password_item = driver.find_element(by=By.ID, value='loginPassword')
    print(password_item.text)
    password_item.send_keys(password);sleep(1)

    login = '''
    
        Log In
      
  '''
    login_item = driver.find_element(by=By.XPATH, value=f'//button[contains(text(),\'{login}\')]')
    print(login_item.text)
    login_item.click(); sleep(3)

def upvote(driver, post_link):
    driver.get(post_link); sleep(1)
    
    upvote_path = '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[1]/div/button[1]/span/i'
    upvote = driver.find_element(by=By.XPATH, value=upvote_path)
    upvote.click()

    
def main():
    driver_file = ChromeDriverManager().install()
    users = pd.read_csv('users.csv', sep=',').iloc[2:]
    post_link = 'https://www.reddit.com/user/craxiss/comments/w26sda/deneme/'
    
    for username, password in zip(users['username'], users['password']): 
        try:
            driver = webdriver.Chrome(driver_file)
            login(driver, username, password)
            upvote(driver, post_link)
        except:
            pass

if __name__ == '__main__':
    main()