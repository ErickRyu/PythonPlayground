from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

main_url = 'http://mobile.kyobobook.co.kr/'
keyword = '코스모폴리스'

driver = wd.Chrome(executable_path='../common/Selenium/chromedriver')
driver.get(main_url)
# id = SearchGNBText

#driver.find_element_by_id('SearchGNBText').send_keys(keyword)
#driver.find_element_by_css_selector('button.search-btn').click()
