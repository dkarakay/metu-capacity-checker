import time
import os

from selenium import webdriver

driver_path = "/Users/sedna/chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)

web_site = "https://sis.metu.edu.tr/get.php?package=-61WpvQxa3pjp9nkYWGoWkJLjUQew_4jPmQNlJf1_nCS4_CpVuwmJkHdZsh9KV5OHAZYt6pSaWlUijcU6m1JFw#/?selectSemester=20212&selectProgram=567&submitSearchForm=Search&stamp=J2897QVVqD0sL0T_kh0fjGaudRH3xqIcG2kcbGtMeh84QMmmR2bmTQ-20bF4RMwamAgJYPa_bqXYoVxSlC9qVg"
driver.get(web_site)
time.sleep(12)
class_index = 51
js = [
    'document.getElementById("SearchResults_column_toggler").getElementsByClassName("checker")[12].firstChild.firstChild.click();',
    'document.getElementById("SearchResults_column_toggler").getElementsByClassName("checker")[13].firstChild.firstChild.click();',
    f'return document.getElementById("SearchResults").rows[{class_index}].getAttribute("key")',
    f'return document.getElementById("SearchResults").rows[{class_index}].children[6].textContent',
    f'return document.getElementById("SearchResults").rows[{class_index}].children[7].textContent',
]
driver.execute_script(js[0])
driver.execute_script(js[1])

while True:
    name = driver.execute_script(js[2])
    capacity = int(driver.execute_script(js[3]))
    used = int(driver.execute_script(js[4]))
    if capacity == 0:
        os.system('say "0 capacity"')
    elif capacity - used > 0:
        os.system(f'say "Found capacity {capacity - used}"')
    elif capacity == used:
        os.system('say "Capacity full"')
    print(f"{name} Cap:{capacity} Used:{used}")
    driver.refresh();
    time.sleep(7)
