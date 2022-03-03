from core.main import auto_checker

semester = '20212'  # 2021-2022 Spring
department_code = '567'  # Electrical Electronics Engineering
class_code = '314'  # Digital Circuits Laboratory
section_no = 8  # Section 8

driver_path = "/Users/sedna/chromedriver"
refresh_rate = 7  # Check each 7 seconds

auto_checker(
    class_code=class_code,
    department_code=department_code,
    driver_path=driver_path,
    refresh_rate=refresh_rate,
    section_no=section_no,
    semester=semester,
    voice_feedback=True,
)
