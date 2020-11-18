from selenium import webdriver
import logging

logger = logging.getLogger('simple_example')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
fh = logging.FileHandler('Test2ChromeLog.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)

driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver.exe')

logger.info('Przejscie na stronę OLX')
driver.get('https://www.olx.pl/')
logger.info('Akceptacja Cookie')
temp = driver.find_element_by_id('onetrust-accept-btn-handler')
temp.click()
logger.info('Przejscie do wszystkich ofert')
temp = driver.find_element_by_id('homeShowAllAds')
temp.click()
logger.info('Wpisanie danych')
temp = driver.find_element_by_id('search-text').send_keys('Golf 6')
temp = driver.find_element_by_id('cityField').send_keys('Gdansk')
temp = driver.find_element_by_id('search-submit')
temp.click()
logger.info('Otrzymanie wyników')


driver.close()
