import smtplib
import appium
import time
import os
import requests
from appium import webdriver
import datetime

fromaddress = 'paparadmy1@gmail.com'
toaddress = 'bansiang.kang@my.panasonic.com'

emailUsername = 'paparadmy1@gmail.com'
emailPassword = '@12345678aA'

os.system("start /B start cmd.exe @cmd /k appium")
desired_caps = {}
desired_caps['automationName'] = 'UiAutomator2'
#change this
desired_caps['platformName'] = 'Android'
#change this
desired_caps['platformVersion'] = '11.0'
#df = pd.read_csv("Test_Cases.csv", index_col = 0)
desired_caps['appPackage'] = 'com.panasonic.ACCsmart'
desired_caps['appActivity'] = 'com.panasonic.ACCsmart.ui.login.LogoStartActivity'
desired_caps['deviceName'] = 'Android Emulator'
#change this
desired_caps['avd'] = 'Gadget3'
desired_caps['avdLaunchTimeout'] = 15000000

errorstage = ""
tickStart = 0
tickEnd = 0
while True:
    errorstage = "No internet connection error"
    tickStart = time.time()
    try:
        r = requests.head(url = 'http://www.google.com/', timeout=5)
        try:
            errorstage = "login page Panasonic ID username click error"
            driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            driver.implicitly_wait(15)
            driver.find_element_by_id("com.panasonic.ACCsmart:id/login_activity_id_edit").click()
            driver.hide_keyboard()
            driver.find_element_by_id("com.panasonic.ACCsmart:id/login_activity_id_edit").send_keys('wirelesstest2018@gmail.com')
            time.sleep(1)
            errorstage = "login page Panasonic ID password click error"
            driver.find_element_by_id("com.panasonic.ACCsmart:id/login_activity_psw_edit").click()
            driver.hide_keyboard()
            driver.find_element_by_id("com.panasonic.ACCsmart:id/login_activity_psw_edit").send_keys('12345678i')
            time.sleep(8)
            errorstage = "login page Panasonic ID remember click error"
            driver.find_element_by_id("com.panasonic.ACCsmart:id/login_activity_remember_cb").click()
            time.sleep(1)
            errorstage = "login page Panasonic ID login click error"
            driver.find_element_by_id("com.panasonic.ACCsmart:id/login_activity_login_btn").click()
            time.sleep(8)
            tickEnd = time.time()
            errorstage = "Home page air cond click error"
            driver.find_element_by_xpath("//android.widget.TextView[@text='Pana_Home']").click()
            time.sleep(8)
            errorstage = "Main page ON OFF button click error"
            driver.find_element_by_id("com.panasonic.ACCsmart:id/view_temp_switch").click()
            time.sleep(10)  
            driver.implicitly_wait(15)
            errorstage = "OK"
            Webelement_error = driver.find_element_by_id("com.panasonic.ACCsmart:id/dialog_common_message")
            print('Testerror : ' + Webelement_error.text)
            if 'server' in Webelement_error.text:
                print('server')
                
                smsmsg = "server error detected, login time:" + str(tickEnd - tickStart) + "Secs" 
                
                try:
                    emailServer = smtplib.SMTP('smtp.gmail.com', 587)
                    emailServer.ehlo()
                    emailServer.starttls()
                    emailServer.login(emailUsername, emailPassword)
                    emailServer.sendmail(fromaddress, toaddress, smsmsg)
                    emailServer.quit()
                except:
                    print("Email Error")
            elif 'Server' in Webelement_error.text:
                print('Server')
                smsmsg = "Server error detected, login time:"  + str(tickEnd - tickStart) + "Secs"
                
                try:
                    emailServer = smtplib.SMTP('smtp.gmail.com', 587)
                    emailServer.ehlo()
                    emailServer.starttls()
                    emailServer.login(emailUsername, emailPassword)
                    emailServer.sendmail(fromaddress, toaddress, smsmsg)
                    emailServer.quit()
                except:
                    print("Email Error")
            elif 'Network' in Webelement_error.text:
                print('Network')
                smsmsg1 = "Network error detected, login time:" + str(tickEnd - tickStart) + "Secs"
                
                try:
                    emailServer = smtplib.SMTP('smtp.gmail.com', 587)
                    emailServer.ehlo()
                    emailServer.starttls()
                    emailServer.login(emailUsername, emailPassword)
                    emailServer.sendmail(fromaddress, toaddress, smsmsg1)
                    emailServer.quit()
                except:
                    print("Email Error")
                #email msg is internet error
        except:
            tickEnd = time.time()
            print("Retry. " + errorstage + str(datetime.datetime.now()))
            if errorstage != "OK" and errorstage != "No internet connection error":
                smsmsg1 = "System error detected," + errorstage + ",  login time:"  + str(tickEnd - tickStart) + "Secs"
                try:
                    emailServer = smtplib.SMTP('smtp.gmail.com', 587)
                    emailServer.ehlo()
                    emailServer.starttls()
                    emailServer.login(emailUsername, emailPassword)
                    emailServer.sendmail(fromaddress, toaddress, smsmsg1)
                    emailServer.quit()
                except:
                    print("Email Error")
                    
    #return True         
    
    except requests.ConnectionError as ex:
       
         tickEnd = time.time()
         print(ex)
    #return False
        
    driver.close_app()
    time.sleep(600)