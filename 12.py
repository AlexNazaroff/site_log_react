
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#driver = webdriver.Firefox()

driver=webdriver.Chrome()
#wait = WebDriverWait(driver, 20)

#driver.implicitly_wait(20) # seconds

#driver.get("http://somedomain/url_that_delays_loading")
#myDynamicElement = driver.find_element_by_id("myDynamicElement")

#driver.get('http://www.python.org')


driver.get('http://board.orsk.ru/')
driver.find_element_by_link_text("Личный кабинет").click()
driver.find_element_by_id("loginform-username").send_keys("LiNi") # Ввод символов

#driver.find_element_by_link_text("Войдите").click()
driver.find_element_by_id("loginform-password").send_keys("q24t4wy554"+'\n') # Ввод символов

# driver.find_element_by_id("loginform-password").send_keys("q24t4wy554"+'/n') # Ввод символов
#driver.find_element_by_link_text("Войти").click()
driver.find_element_by_xpath("//*[@id='submit']/input[@type='checkbox']").click()
# submit
