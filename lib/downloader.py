import os
import time
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait

def get_excel(driver, download_path):
    file_path = os.path.join(download_path , 'tumhisse.xlsx')
    try:
        WebDriverWait(driver, 30).until(lambda d: os.path.exists(file_path))
    except:
        print('Waiting For File To Download...')
        time.sleep(10)

    read_file = pd.read_excel(file_path)
    # Change column names to english for data processing.
    file = read_file.rename(
        columns={'Tarih': 'Date', 'Kapanış(TL)': 'Close', 'Min(TL)': 'Low', 'Max(TL)': 'High', 'AOF(TL)': 'Open',
                 'Hacim(TL)': 'Volume'})
    return file