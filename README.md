# METU Auto Capacity Checker

## Installation
- Download **Chrome Webdriver** or **Firefox Geckodriver**
- Locate it somewhere to easily reach
- Create Python environment using ```mkvirtualenv capacity-checker -p Python3```
- Inside the environment, install requirements ```pip install -r requirements.txt```
- Modify _necessary parameters_ inside **run.py**
- Run ```python run.py```
- When the browser is opened, change _Display records_ per page from 10 to **All** [[Screenshot](https://user-images.githubusercontent.com/20050426/156389364-8a6e12b7-16e9-47fe-9847-4fc70d323e80.png)]
- Type ```ok``` in terminal and hit enter
- Enjoy ☕️

## Parameters

- ```class_code``` Class code _e.g. 201 (Circuit 1)_  **(string)**
- ```department_code``` Department code _e.g. 567 (Electrical Electronics Engineering)_ **(string)**
- ```driver_path``` Chromedriver or Firefox Driver path **(string)**
- ```refresh_rate``` Refresh rate for checker in seconds _e.g. 5_  **(int)**
- ```section_no``` Section no _e.g. 1_ **(int)**
- ```semester``` Semester code _e.g. 20212 (2021-2022 Spring)_ **(string)**
- ```voice_feedback``` True if you want voice feedback _tested only on macOS_ **(bool)**

## Notes

- Based on [Sis METU](http://sis.metu.edu.tr/)
- Used Chromedriver version: _ChromeDriver 99.0.4844.51_ but others will work
- Voice feedback is tested only on **macOS**
- Download the latest or suitable version for Chrome from https://chromedriver.chromium.org/downloads
- Download the latest or suitable version for Firefox Geckodriver from https://github.com/mozilla/geckodriver/releases
