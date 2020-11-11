from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.action_chains import ActionChains


opt=Options()
opt.add_argument('start-maximized')

driver=webdriver.Chrome(chrome_options=opt,executable_path='C:\Program Files (x86)\chromedriver.exe')
driver.get('https://orteil.dashnet.org/cookieclicker/beta/')
time.sleep(5)
print(driver.title)

for i in range(5000):
    #For clicking the cookie
    cookie=driver.find_element_by_id('bigCookie')
    cookie.click()
    cookieCount=int(driver.find_element_by_id('cookies').text.split(' ')[0].replace(',',''))

    #For locating Cursor powerup
    if driver.find_element_by_xpath('//*[@id="product0"]') and cookieCount>=int(driver.find_element_by_xpath('//*[@id="productPrice0"]').text.replace(',','')):
        item=driver.find_element_by_xpath('//*[@id="productPrice0"]')
        actions = ActionChains(driver)
        actions.move_to_element(item)
        actions.click()
        actions.move_to_element(cookie)
        actions.perform()
    #For locating Grandma powerup
    elif ((driver.find_element_by_xpath('//*[@id="productPrice1"]').text)!='') and cookieCount>=int(driver.find_element_by_xpath('//*[@id="productPrice1"]').text.replace(',','')):
        item=driver.find_element_by_xpath('//*[@id="productPrice1"]')
        actions = ActionChains(driver)
        actions.move_to_element(item)
        actions.click()
        actions.move_to_element(cookie)
        actions.perform()
    #For locating Farm powerup
    elif ((driver.find_element_by_xpath('//*[@id="productPrice2"]').text)!='') and cookieCount>=int(driver.find_element_by_xpath('//*[@id="productPrice2"]').text.replace(',','')):
        item=driver.find_element_by_xpath('//*[@id="productPrice2"]')
        actions = ActionChains(driver)
        actions.move_to_element(item)
        actions.click()
        actions.move_to_element(cookie)
        actions.perform()
    #For locating Mine powerup
    elif ((driver.find_element_by_xpath('//*[@id="productPrice3"]').text)!='') and cookieCount>=int(driver.find_element_by_xpath('//*[@id="productPrice3"]').text.replace(',','')):
        item=driver.find_element_by_xpath('//*[@id="productPrice3"]')
        actions = ActionChains(driver)
        actions.move_to_element(item)
        actions.click()
        actions.move_to_element(cookie)
        actions.perform()

driver.close()
