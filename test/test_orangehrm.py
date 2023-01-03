from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

def test_tc002() :


    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    driver.implicitly_wait(5)
    driver.maximize_window()

    username = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
    password = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
    login = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
    abc = "//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p"
    logout = "//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a"
    title = "OrangeHRM"


    time.sleep(3)
    driver.find_element_by_xpath(username).send_keys("Admin")

    time.sleep(3)
    driver.find_element_by_xpath(password).send_keys("admin123")

    time.sleep(2)
    driver.find_element_by_xpath(login).click()

    time.sleep(2)
    driver.find_element_by_xpath(abc).click()

    time.sleep(2)
    driver.find_element_by_xpath(logout).click()

    driver.quit()



# actual_value = driver.title
# expected ="OrangeHRM"
#
# print(actual_value)
#
# assert expected == actual_value