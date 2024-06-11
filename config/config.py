import logging
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

URL = 'https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/Tarihsel-Fiyat-Bilgileri.aspx'
HEADLESS = '--headless=new'
WEB_DRIVER_PATH = 'C:/Users/ahmet/OneDrive/Desktop/chromedriver.exe'
WEB_WAIT_EX = config['DEFAULT'].getint('WEB_WAIT_EX')
USER_AGENT = config['DEFAULT']['USER_AGENT']
WEB_WAIT = config['DEFAULT'].getint('WEB_WAIT')

# Logging Configuration
logging.basicConfig(level=logging.WARNING)
LOGGER = logging.getLogger('selenium.webdriver.remote.remote_connection')
LOGGER.setLevel(logging.WARNING)