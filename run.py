from core.main import auto_checker_capacity

semester = '20222'  # 2022-2023 Spring
department_code = '567'  # Electrical Electronics Engineering
class_code = '314'  # Digital Circuits Laboratory
section_no = 8  # Section 8

driver_path = "/Users/sedna/local-dev/chromedriver"
refresh_rate = 4  # Check each 4 seconds

discord_webhook_url = 'https://discord.com/api/webhooks/xxxx'

# Deprecated for now

# auto_checker(
#     class_code=class_code,
#     department_code=department_code,
#     discord_bot=False,
#     discord_webhook_url=discord_webhook_url,
#     driver_path=driver_path,
#     refresh_rate=refresh_rate,
#     section_no=section_no,
#     semester=semester,
#     telegram_bot=False,
#     voice_feedback=True,
# )

# Check capacity increase
auto_checker_capacity(
    class_code=class_code,
    department_code=department_code,
    discord_bot=False,
    discord_webhook_url=discord_webhook_url,
    driver_path=driver_path,
    refresh_rate=refresh_rate,
    section_no=section_no,
    semester=semester,
    voice_feedback=True,
    first_time=True,
    # telegram_bot=False,
)
