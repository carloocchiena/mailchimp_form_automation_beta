'''
created by carlo occhiena on dec 2020
'''

from selenium import webdriver   #to handle chromium webdriver

#load the chrome webdriver (get the right one from https://chromedriver.chromium.org/downloads)
browser = webdriver.Chrome("D:\yourpath\chromedriver.exe")

'''
Testing newsletter form 
'''


#open the webpage
browser.get("http://www.yoursite.com")

#login info
mailID = browser.find_element_by_id("mce-EMAIL")
mailID.send_keys("ceo@mail.com")

nameID = browser.find_element_by_id("mce-NOME")
nameID.send_keys("super mario bros")

nameID.submit()
