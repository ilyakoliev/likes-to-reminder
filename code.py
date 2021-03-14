from selenium.webdriver import Chrome
import time

path = 'PATH_TO_CHROMEDRIVER'
likes = int(input('How many likes? '))
post = input('Link to the post: ')

def check():
    try:
        driver.find_element_by_class_name('_subscription__button_5baba').click()
    except:
        print('Email request not found')

for i in range(int(likes / 5)):
    driver = Chrome(executable_path=path)
    time.sleep(2)
    driver.get(post)
    time.sleep(2)
    element = driver.find_element_by_class_name('_inner_8b2d8')
    element.location_once_scrolled_into_view
    check()
    for i in range(5):
        driver.find_element_by_class_name('_inner_8b2d8').click()
    driver.close()
    time.sleep(1)

driver = Chrome(executable_path=path)
time.sleep(2)
driver.get(post)
time.sleep(2)
element = driver.find_element_by_class_name('_inner_8b2d8')
element.location_once_scrolled_into_view
check()
for i in range(likes % 5):
    driver.find_element_by_class_name('_inner_8b2d8').click()
driver.close()
