# METU Auto Capacity Checker

## Installation

- Download **Chrome Webdriver** or **Firefox Geckodriver**
- Locate it somewhere to easily reach
- Create Python environment using ```mkvirtualenv capacity-checker -p Python3```
- Inside the environment, install requirements ```pip install -r requirements.txt```
- Modify _necessary parameters_ inside **run.py**
- Run ```python run.py```
- ~~When the browser is opened, change _Display records_ per page from 10 to All~~
- Thanks to [@ardaozarslan](https://github.com/ardaozarslan) for his great contribution!
- When the website is loaded correctly, type ```ok``` in terminal and hit enter
- Enjoy ☕️

## Telegram Installation

- Create a bot on Telegram talking with BotFather
- Run ```telegram-send --configure``` on terminal
- Insert the created bot token
- Enter the shown password in your Telegram Chat
- Voila 🎉

## Parameters

| Parameter                 | Type   | Notes                                                                     |
|---------------------------|--------|---------------------------------------------------------------------------|
| ```class_code```          | string | Class code  _e.g. 201 (Circuit 1)_                                        |
| ```department_code```     | string | Department code _e.g. 567 (Electrical Electronics Engineering)_           |
| ```discord_bot```         | bool   | True if you want Discord Message from your server for available capacity. |
| ```discord_webhook_url``` | string | Webhook URL for discord                                                   |
| ```driver_path```         | string | Chromedriver or Firefox Driver path                                       |
| ```refresh_rate```        | int    | Refresh rate for checker in seconds _e.g. 5_                              |
| ```section_no```          | int    | Section no _e.g. 1_                                                       |
| ```semester```            | string | Semester code _e.g. 20212 (2021-2022 Spring)_                             |
| ```telegram_bot```        | bool   | True if you want Telegram Message for available capacity.                 |
| ```voice_feedback```      | bool   | True if you want voice feedback. _Tested only on macOS_                   |

## Notes

- Based on [Sis METU](http://sis.metu.edu.tr/)
- Used Chromedriver version: _ChromeDriver 99.0.4844.51_ but others will work
- Voice feedback is tested only on **macOS**
- Download the latest or suitable version for Chrome from https://chromedriver.chromium.org/downloads
- Download the latest or suitable version for Firefox Geckodriver from https://github.com/mozilla/geckodriver/releases
