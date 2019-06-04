from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import re

login_url = 'https://www.instagram.com/accounts/login/?source=auth_switcher'
keyword = 'weedle'

tag_url = 'https://www.instagram.com/explore/tags/'
search_url = tag_url + keyword + '/'

insta_id = 'hwoong@gmail.com'
insta_pw = 'xjfdjqt1'

browser = wd.Chrome(executable_path='../common/Selenium/chromedriver')
browser.get(login_url)

WebDriverWait(browser, 10)

browser.find_elements_by_css_selector('form input')[0].send_keys(insta_id)
browser.find_elements_by_css_selector('form input')[1].send_keys(insta_pw)

browser.find_elements_by_css_selector('form button')[1].click()

time.sleep(3)

WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Not Now')]"))).click()

browser.get(search_url)

links = list()
source = browser.page_source
data = bs(source, 'html.parser')
body = data.find('body')
script = body.find('span')
for link in script.findAll('a'):
    if re.match("/p", link.get('href')):
        links.append('https://www.instagram.com'+link.get('href'))

for link in links:
    print(link)

#browser.get(links[1])
print(urlopen(links[1]).read())
