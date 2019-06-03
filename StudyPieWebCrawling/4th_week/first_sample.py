from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

main_url = 'https://tour.interpark.com/'
keyword = '덴마크'

driver = wd.Chrome(executable_path='../common/Selenium/chromedriver')
driver.get(main_url)
# id = SearchGNBText

driver.find_element_by_id('SearchGNBText').send_keys(keyword)
driver.find_element_by_css_selector('button.search-btn').click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(By.CLASS_NAME, 'panelZone')
    )
except Exception as e:
    print('error occurred', e)

driver.find_element_by_css_selector('.panelZone>.oTravelBox>.boxList>.moreBtnWrap>.moreBtn').click()

