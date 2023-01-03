from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

def test_tc001_get() :
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    driver.implicitly_wait(5)

    username = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
    password = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
    login = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
    paul = "//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p"
    admin = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span"
    logout = "//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a"


    time.sleep(3)
    driver.find_element_by_xpath(username).send_keys("Admin")

    time.sleep(3)
    driver.find_element_by_xpath(password).send_keys("admin123")

    time.sleep(3)
    driver.find_element_by_xpath(login).click()

    time.sleep(2)
    driver.find_element_by_xpath(admin).click()

    time.sleep(2)
    driver.find_element_by_xpath(paul).click()

    time.sleep(2)
    driver.find_element_by_xpath(logout).click()

    driver.quit()

# # chrome_driver = 'C:\\Users\\Ferdous Ahmed\\Desktop\\ui_spectrum\\chromedriver_win32 (2)\\chromedriver.exe'
# chrome_driver = r'C:\Users\Ferdous Ahmed\Desktop\ui_spectrum\chromedriver_win32 (2)\chromedriver.exe'
# # chrome_driver = 'C:/Users/Ferdous Ahmed/Desktop/ui_spectrum/chromedriver_win32 (2)/chromedriver.exe'
#
# driver = webdriver.Chrome(chrome_driver)
#
# #driver.get("https://www.facebook.com/")
# driver.get("https://opensource-demo.orangehrmlive.com/")
# #driver.get("http://localhost:8888/spectrum")
#
# print('This is Title :', driver.title)


# from selenium import webdriver
#
# chrome_driver = r'C:\Users\Ferdous Ahmed\Desktop\ui_spectrum\chromedriver_win32 (2)\chromedriver.exe'
#
# driver = webdriver.Chrome(chrome_driver)
# driver.get("https://opensource-demo.orangehrmlive.com/")

# from selenium import webdriver
# chrome_driver = r'C:\Users\Ferdous Ahmed\Desktop\ui_spectrum\chromedriver_win32 (2)\chromedriver.exe'
# driver = webdriver.Chrome(chrome_driver)








