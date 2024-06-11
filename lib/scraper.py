import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from config import config

def setup_driver():
    options = Options()
    if config.USER_AGENT != '':
        options.add_argument(f'user-agent={config.USER_AGENT}')
    options.add_argument(config.HEADLESS)
    driver = webdriver.Chrome(executable_path = ChromeDriverManager().install(),options=options)
    return driver

def choose_pair(driver,  pair_name , year , month):
    driver.get(config.URL)
    WebDriverWait(driver, config.WEB_WAIT).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl00_ctl58_g_0d19e9f2_2afd_4e5a_9a92_57c4ab45c57a"]/div/div/div[1]/div/div/div[1]/span/span[1]/span/span[2]/b'))
    ).click()
    driver.find_element(By.CLASS_NAME, 'select2-search__field').send_keys(pair_name)
    driver.find_element(By.CLASS_NAME, 'select2-search__field').send_keys(Keys.ENTER)

    date_picker = WebDriverWait(driver, config.WEB_WAIT).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#dtStartDateHisse')))
    time.sleep(config.WEB_WAIT_EX)
    date_picker.click()

    # Select Year
    while True:
        select_year = Select(WebDriverWait(driver, config.WEB_WAIT).until(EC.element_to_be_clickable((By.CLASS_NAME, 'picker__select--year'))))
        options = select_year.options
        if year in [option.text for option in options]:
            select_year.select_by_visible_text(year)
            break
        else:
            select_year.select_by_visible_text(options[0].text)

    # Select Month
    select_month = Select(WebDriverWait(driver, config.WEB_WAIT).until(EC.element_to_be_clickable((By.CLASS_NAME, 'picker__select--month'))))
    select_month.select_by_visible_text(month)

    # Select Day
    time.sleep(config.WEB_WAIT_EX)
    WebDriverWait(driver, config.WEB_WAIT).until(
        EC.element_to_be_clickable((By.XPATH, f'//*[@id="dtStartDateHisse_table"]/tbody/tr[1]/td[5]/div'))
    ).click()

    # Click to get data
    time.sleep(config.WEB_WAIT_EX)
    WebDriverWait(driver, config.WEB_WAIT).until(EC.element_to_be_clickable(
        (By.ID, 'btnGetHisseTekil')
    )).click()

    # Wait and download the file
    time.sleep(config.WEB_WAIT_EX)
    WebDriverWait(driver, config.WEB_WAIT).until(EC.element_to_be_clickable((By.CLASS_NAME, 'excelimage'))).click()
    time.sleep(10)