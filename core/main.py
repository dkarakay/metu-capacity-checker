import time
import os
from selenium import webdriver
from datetime import datetime
import core.js_codes as js


def auto_checker(
        class_code: str,
        department_code: str,
        driver_path: str,
        refresh_rate: int,
        section_no: int,
        semester: str,
        voice_feedback: bool,
):
    # Run Chrome Driver
    driver = webdriver.Chrome(executable_path=driver_path)

    key_code = f'{department_code}0{class_code}|{semester}|{department_code}|{section_no}'

    # Open website sis.metu.edu.tr
    web_site = f"https://sis.metu.edu.tr/get.php?package" \
               f"=-61WpvQxa3pjp9nkYWGoWkJLjUQew_4jPmQNlJf1_nCS4_CpVuwmJkHdZsh9KV5OHAZYt6pSaWlUijcU6m1JFw#/?selectSemester" \
               f"={semester}&selectProgram={department_code}&submitSearchForm=Search"
    driver.get(web_site)

    while True:
        # Type ok when you select display all
        if input('Enter "ok" if you display all courses: ') == 'ok':
            break

    for i in js.show:
        driver.execute_script(i)

    print(key_code)

    # Get index script
    js_key = js.get_index(key_code=key_code)

    try:
        class_index = int(driver.execute_script(js_key))

        # For getting correct section
        class_index += 1

        js_name, js_cap, js_used = js.get_data(class_index=class_index)

        while True:
            name = driver.execute_script(js_name)
            capacity = int(driver.execute_script(js_cap))
            used = int(driver.execute_script(js_used))

            if voice_feedback:
                # Voice feedback for macOS
                if capacity == 0:
                    os.system('say "0 capacity"')
                elif capacity - used > 0:
                    os.system(f'say "Found capacity {capacity - used}"')
                elif capacity == used:
                    os.system('say "Capacity full"')

            # Get current time
            current_time = datetime.now().time()

            # Print current of the course
            print(f"{current_time} - {name} Cap:{capacity} Used:{used}")

            # Refresh page
            driver.refresh()

            # Refresh rate
            time.sleep(refresh_rate)

    except:
        print("Please check course details and try again")
