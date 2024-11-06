from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import TimeoutException
from data import *
import string
import random
import os
import time



files = os.listdir()
files = [x for x in files if x.endswith('pdf')]
for x in files:
    os.remove(x) 


chrome_options = Options()
chrome_options.headless = False
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])
chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "download.default_directory": "C:\\Users\\omer.adiguzel\\Desktop\\RPA-Selenium\\",
        "download.prompt_for_download": False,
        'profile.default_content_setting_values.automatic_downloads': 1,
        "profile.password_manager_enabled": False
})

driver = webdriver.Chrome(service=ChromeService(executable_path='chromedriver.exe'), options=chrome_options)
driver.get('*****')
driver.maximize_window()


WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath_username))).clear()
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath_username))).send_keys(username)
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath_password))).clear()
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath_password))).send_keys(password)
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath_login_button))).click()
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath_izinler_button))).click()
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath_izinlerim_button))).click()
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath_pdf_button))).click()
time.sleep(2)


driver.get(url_ghub)
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath_ghub_login))).clear()
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath_ghub_login))).send_keys(username_ghub)
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath_ghub_password))).clear()
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath_ghub_password))).send_keys(password_ghub)
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath_ghub_login_button))).click()
auth_code = int(input('Authentication code giriniz : '))
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath_ghub_auth))).send_keys(auth_code)
try:
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, xpath_ghub_auth_login_button))).click()
except:
    pass
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath_ghub_new_repo_button))).click()

repo_name = ''.join(random.choices(string.ascii_lowercase +
                             string.digits, k=8))

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath_ghub_create_repo_name))).send_keys(repo_name)
time.sleep(2.5)
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath_ghub_create_repo_submit_button))).click()
time.sleep(5)
driver.get(url_ghub_upload.format(repo_name))

files = [x for x in os.listdir() if x.endswith('pdf')]
filename = "C:\\Users\\omer.adiguzel\\Desktop\\RPA-Selenium\\" + files[0]


WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath_ghub_upload_field))).send_keys(filename)
time.sleep(10)
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath_ghub_upload_commit_button))).click()
time.sleep(20)
driver.quit()
