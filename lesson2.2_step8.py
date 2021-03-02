from selenium import webdriver
import os, time


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_name("firstname")
input1.send_keys("Ivan")
input2 = browser.find_element_by_name("lastname")
input2.send_keys("Ivanov")
input3 = browser.find_element_by_name("email")
input3.send_keys("Ivan@mail.ru")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
input4 = browser.find_element_by_name("file")
input4.send_keys(file_path)
button = browser.find_element_by_tag_name("button")
button.click()
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()
