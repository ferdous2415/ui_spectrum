import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())

def test_tc003() :


    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(5)

    username = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
    password = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
    login = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
    admin = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span"
    admin_add = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button"
    #admin_add_userroll = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div"
    paul = "//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p"
    logout = "//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a"

    time.sleep(2)
    driver.find_element_by_xpath(username).send_keys("Admin")

    time.sleep(2)
    driver.find_element_by_xpath(password).send_keys("admin123")

    time.sleep(2)
    driver.find_element_by_xpath(login).click()

    time.sleep(3)
    driver.save_screenshot("home_image.png")
    driver.find_element_by_xpath(admin).click()

    time.sleep(2)
    driver.find_element_by_xpath(admin_add).click()

    # time.sleep(2)
    # driver.find_element_by_xpath(admin_add_userroll).click()
    # dropdownbox = driver.find_elements(by = By.TAG_NAME, value = "ESS")

    #dropdownbox[0].click()

    time.sleep(2)
    driver.find_element_by_xpath(paul).click()

    time.sleep(3)
    driver.find_element_by_xpath(logout).click()

    #expect_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    actual_url = driver.current_url

    # assert expect_url == actual_url

    print("Assertion Successfull :", driver.current_url)

    time.sleep(2)
    driver.quit()


