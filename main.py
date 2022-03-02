import time
import os
from selenium import webdriver
from datetime import datetime

# Download specific browser driver and give its path
driver_path = "/Users/sedna/chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)

# Sis website link
department_code = '567'  # Electrical Electronics Engineering
semester = '20212'  # 2021-2022 Spring
class_index = 51

refresh_rate_per_second = 7

web_site = f"https://sis.metu.edu.tr/get.php?package" \
           f"=-61WpvQxa3pjp9nkYWGoWkJLjUQew_4jPmQNlJf1_nCS4_CpVuwmJkHdZsh9KV5OHAZYt6pSaWlUijcU6m1JFw#/?selectSemester" \
           f"={semester}&selectProgram={department_code}&submitSearchForm=Search"
driver.get(web_site)

while True:
    # Type ok when you select display all
    if input('enter if you entered all places correctly: ') == 'ok':
        break

js = [
    # Show Capacity
    'document.getElementById("SearchResults_column_toggler").getElementsByClassName("checker")[12].firstChild.firstChild.click();',

    # Show Used Capacity
    'document.getElementById("SearchResults_column_toggler").getElementsByClassName("checker")[13].firstChild.firstChild.click();',

    # Get name & capacity & used capacity info for specified class & section
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

    # Voice based output for OS & Linux
    if capacity == 0:
        os.system('say "0 capacity"')
    elif capacity - used > 0:
        os.system(f'say "Found capacity {capacity - used}"')
    elif capacity == used:
        os.system('say "Capacity full"')

    current_time = datetime.now().time()

    # Print details of the course
    print(f"{current_time} - {name} Cap:{capacity} Used:{used}")

    driver.refresh();
    time.sleep(refresh_rate_per_second)
