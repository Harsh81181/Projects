from selenium import webdriver
browser=webdriver.Chrome("Enter_webdriver_path")
browser.maximize_window()
browser.get("Website_Login_page_link")
uname=browser.find_element_by_id("Username_or_email")
pswrd=browser.find_element_by_id("password")
btn=browser.find_element_by_id("login_btn")
uname.send_keys("Enter_Your_Username_or_email")
pswrd.send_keys("Enter_password")
btn.click()

#code is written by Harsh Bhardwaj
