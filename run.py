from core.main import auto_checker

semester = '20212'  # 2021-2022 Spring
department_code = '567'  # Electrical Electronics Engineering
class_code = '314'  # Digital Circuits Laboratory
section_no = 8  # Section 8

driver_path = "/Users/sedna/chromedriver"
refresh_rate = 7  # Check each 7 seconds

discord_webhook_url = 'https://discord.com/api/webhooks/xxxx'

auto_checker(
    class_code=class_code,
    department_code=department_code,
    discord_bot=True,
    discord_webhook_url=discord_webhook_url,
    driver_path=driver_path,
    refresh_rate=refresh_rate,
    section_no=section_no,
    semester=semester,
    telegram_bot=True,
    voice_feedback=True,
)
