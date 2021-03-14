from selenium.webdriver import Chrome
import time

path = 'PATH_TO_CHROMEDRIVER'
likes = int(input('How many likes? '))
post = input('Link to the post: ')

for i in range(int(likes / 5)):
    driver = Chrome(executable_path=path)
    time.sleep(2)
    driver.get(post)
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 5000);")
    driver.execute_script("window.scrollTo(0, -500);")
    time.sleep(2)
    try:
        driver.find_element_by_class_name('_subscription__button_5baba').click()
    except:
        print('Email request not found')
    for i in range(5):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    for i in range(5):
        driver.find_element_by_class_name('_inner_8b2d8').click()
    time.sleep(2)
    driver.close()
    time.sleep(2)

driver = Chrome(executable_path=path)
time.sleep(2)
driver.get(post)
time.sleep(2)
driver.execute_script("window.scrollTo(0, 5000);")
driver.execute_script("window.scrollTo(0, -500);")
time.sleep(2)
try:
    driver.find_element_by_class_name('_subscription__button_5baba').click()
except:
    print('Email request not found')
for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
for i in range(likes % 5):
    driver.find_element_by_class_name('_inner_8b2d8').click()
time.sleep(2)
driver.close()
