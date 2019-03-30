#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#Config==============================================
url = 'www.baidu.com'
driver = webdriver.Chrome()
titleCheckString = u"百度一下"

#Function Delaration=================================
#Click on Login button
def login():
    loginbymain = driver.find_element_by_xpath("//*[@id='u1']/a[7]").click()

#Click on by account
def loginbyaccount():
    pressloginbyaccount = driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_10__footerULoginBtn']").click()


#Test Case=============================================
# Step1: Enter url
driver.get('https://www.baidu.com')
time.sleep(5)
# Verify title name of url
try:
    assert titleCheckString in driver.title
    print('Successful Log in Main')

except Exception as e:
    print('Title is not matching with Main page')

# Step2: Click on Log in
time.sleep(5)
login()
print('Click on LogIn button')

#Step3: Click on log in by account
time.sleep(5)
loginbyaccount()
print('Click on by Account')

#Step4: Check whether error message displayed
time.sleep(5)

driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_10__submit']").click()
time.sleep(5)
Error_message = driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_10__error']").text
try:
    assert Error_message == u'请您输入手机/邮箱/用户名'
    print('Success: Error message display correctly.')

except Exception as e:
    print('Fail: Error message does not display')