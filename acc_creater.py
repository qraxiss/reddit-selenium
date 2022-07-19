from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from string import digits, ascii_letters
from selenium import webdriver
from secrets import choice
from random import randint
from os import listdir
from time import sleep


def user_generator(driver, alphabet):
    driver.get('https://en.wikipedia.org/wiki/Special:Random')
    name = driver.find_element(by=By.CLASS_NAME, value="firstHeading").text[:randint(5,7)].replace(' ', '') + str(randint(10000,99999))
    password = ''.join(choice(alphabet) for i in range(16))

    return name, password

def create_acc(driver, name, password):
    driver.get('https://www.reddit.com/register/')

    mail_item = driver.find_element(by=By.ID, value='regEmail')
    print(mail_item.text)
    mail_item.send_keys(f'{name}@gmail.com'); sleep(1)

    continue_item = driver.find_element(by=By.XPATH, value='//button[contains(text(),\'Continue\')]')
    print(continue_item.text)
    continue_item.click(); sleep(3)

    username_item = driver.find_element(by=By.ID, value='regUsername')
    print(username_item.text)
    username_item.send_keys(name); sleep(1)

    password_item = driver.find_element(by=By.ID, value='regPassword')
    print(password_item.text)
    password_item.send_keys(password); sleep(1)

    sign_up_item = driver.find_element(by=By.CSS_SELECTOR, value='.AnimatedForm__submitButton.SignupButton')
    print(sign_up_item.text)
    sign_up_item.click(); sleep(30)

def main():
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        name, password = user_generator(driver, digits+ascii_letters)
        
        if not 'users.csv' in listdir():
            with open('users.csv', 'w') as file:
                file.write('username,password')

        with open('users.csv', 'a') as file:
            file.write(f'\n{name},{password}')

        create_acc(driver, name, password)
    except:
        pass

if __name__ == '__main__':
    main()