from selenium import webdriver
import time


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_tag_name("button")
button.click()

confirm = browser.switch_to.alert
confirm.accept()

x = browser.find_element_by_id("input_value")


input1.send_keys("Ivan")
input2 = browser.find_element_by_name("lastname")
input2.send_keys("Ivanov")
input3 = browser.find_element_by_name("email")
input3.send_keys("Ivan@mail.ru")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
input4 = browser.find_element_by_name("file")
input4.send_keys(file_path)

time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()
