# import pytest
# from selenium.webdriver.chrome import webdriver
# from selenium import webdriver
#
#
# @pytest.fixture()
# def init_driver(request):
#
#     driver = webdriver.Chrome(executable_path="C:/chromedriver_win32/chromedriver.exe")
#     # driver = webdriver.Chrome(Testdata.CHROME_EXECUTABLE_PATH)
#     # driver.get("https://www.google.com")
#     driver.maximize_window()
#     # driver.implicitly_wait(30)
#     request.cls.driver = driver
#     # return driver
#     yield
#     driver.close()