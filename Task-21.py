from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
# Navigate the URL
driver.get("https://www.saucedemo.com/")
time.sleep(2)  

# Display cookies before login
print("Cookies before login:")
cookies_before = driver.get_cookies()
print(cookies_before)

# Perform login
username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

username.send_keys("standard_user")
password.send_keys("secret_sauce") 
login_button.click()
time.sleep(3)

# Display cookies after login
print("\nCookies after login:")
cookies_after = driver.get_cookies()
print(cookies_after)

# Perform logout
menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
menu_button.click()
time.sleep(1)
logout_button = driver.find_element(By.ID, "logout_sidebar_link")
logout_button.click()
time.sleep(2) 

# Display cookies after logout
print("\nCookies after logout:")
cookies_after_logout = driver.get_cookies()
print(cookies_after_logout)

#If cookies are being generated during login
if cookies_before != cookies_after:
    print("\nCookies have been updated during the login process.")
else:
    print("\nNo changes in cookies during the login process.")

# Close the browser
driver.quit()
