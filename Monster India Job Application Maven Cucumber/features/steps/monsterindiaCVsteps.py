import time
import pytest
from lib2to3.pgen2 import driver

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from Utilities.readproperty import ReadConfigfile

app_Url = ReadConfigfile.getUrl()


@given('launch the chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
    context.driver.maximize_window()


@when('open monsterIndia.com homepage')
def openHomepage(context):
    context.driver.get(app_Url)


# Used Step Parameters to login the Application !!
# @when('login with username "{uname}" and password "{pwd}" & updating Ranees CV on my profile page')

# Used Read properties method to Read Config File !!
@when('login with username and password & updating Ranees CV on my profile page')
def updateingCV(context):
    email = ReadConfigfile.getEmail()
    pwd = ReadConfigfile.getPassword()
    try:
        time.sleep(10)
        context.driver.find_element(By.XPATH, "//*[@id='pop_rea']/div[1]").click()
        print("Foundit Popup Window Successfully Closed")
    except Exception:
        print("Foundit Popup Window closing Failed")
    context.driver.find_element(By.CLASS_NAME, "msite-login").click()

    # Used Step Parameters method to login the Application !!
    # context.driver.find_element(By.ID, "signInName").send_keys(uname)
    # context.driver.find_element(By.ID, "password").send_keys(pwd)

    # Used Read properties method to Read Config File !!
    time.sleep(4)
    context.driver.find_element(By.ID, "signInName").send_keys(email)
    context.driver.find_element(By.ID, "password").send_keys(pwd)
    context.driver.find_element(By.ID, "signInbtn").click()


@then('verify that it must be last updated on: current date')
def verifylastDate(context):
    time.sleep(5)
    context.driver.find_element(By.XPATH, "//i[@class='mqfihd-male-user']").click()
    # context.driver.find_element(By.XPATH, "//button[contains(@class,'line-btn btn-hm-profile')]").click()
    # context.driver.find_element(By.XPATH, "(//i[@class='icon-cross'])[3]").click()
    context.driver.find_element(By.CLASS_NAME, "mqfi-upload").click()
    time.sleep(5)
    uploadresutext_verify= context.driver.find_element(By.XPATH, "//h3[text()='Upload Resume']").text
    if "Upload Resume" in uploadresutext_verify:
        print("Validation Passed")
    else:
        print("Validation Failed")

    time.sleep(4)
    context.driver.find_element(By.ID, "resume").send_keys("C:\\Users\\Ranees\\Desktop\\CV Ranees.pdf")
    time.sleep(4)
    context.driver.find_element(By.XPATH, "(//button[contains(@class,'btn pt10')])[2]").click()
    time.sleep(4)
    lastupdate_verify = context.driver.find_element(By.XPATH, "//span[@class='last-update mt15']").text
    time.sleep(5)
    assert "Last Updated on : 9 December 2022" in lastupdate_verify, "Last Updated Date Verified Not Success"
    print("Last Updated Date Verified Success")
    time.sleep(4)
    context.driver.find_element(By.XPATH, "//div[@id='profileThemeDefault']/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/i[1]").click()


@then('logout the monsterIndia job profile')
def logoutProfile(context):
    time.sleep(5)
    context.driver.find_element(By.XPATH, "(//i[@class='mqfihd-default-profile'])[3]").click()
    context.driver.find_element(By.XPATH, "(//a[@class='logout-link'])[2]").click()


@then('close the browser')
def closeBrowser(context):
    context.driver.close()
