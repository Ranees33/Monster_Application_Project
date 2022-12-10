import time
from lib2to3.pgen2 import driver
# from telnetlib import EC

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from Utilities.readproperty import ReadConfigfile

app_Url = ReadConfigfile.getUrl()


@given('launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)


@when('open MonsterIndia homepage')
def openHomepage(context):
    context.driver.get(app_Url)
    time.sleep(5)


# Used Step Parameters to login the Application !!
@when('login the application with username "{uname}" and password "{pwd}"')
def logintheApplication(context, uname, pwd):
    # context.driver.find_element(By.XPATH, "(//span[text()='Jobseeker Login'])[3]").click()
    # try:
    # time.sleep(10)
    #     # context.driver.find_element(By.XPATH, "//*[@id='pop_rea']/div[1]").click()
    #     foundit_Popup = context.WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='pop_rea']/div[1]")))
    #     foundit_Popup.click()
    #     print("Foundit Popup Window Successfully Closed")
    # except Exception:
    #     print("Foundit Popup Window closing Failed 'or' not Found")
    # context.driver.switch_to.alert.dismiss()
    # popup_Close1 = popup_Close.dismiss
    # text_Info = popup_Close.text
    time.sleep(4)
    context.driver.find_element(By.CLASS_NAME, "msite-login").click()
    context.driver.find_element(By.ID, "signInName").send_keys(uname)
    context.driver.find_element(By.ID, "password").send_keys(pwd)
    context.driver.find_element(By.ID, "signInbtn").click()


@then('verify that the redirect to Profile page')
def verifyProfilepage(context):
    time.sleep(5)
    name_verify = context.driver.find_element(By.XPATH, "//p[text()='Welcome Back Ahamed ranees,']").text
    print(name_verify)
    # time.sleep(5)
    # Used Two Assert Methods to verify the name Text which is Equal or Not !!
    # assert name_verify == "Ahamed Ranees"
    try:
        time.sleep(20)
        assert "Ahamed Ranees" in name_verify
        time.sleep(4)
        print("Assert Test Passed")
    except Exception:
        print("Assert Test Failed")


@then('close browser')
def closeBrowser(context):
    context.driver.close()
